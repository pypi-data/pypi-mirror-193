import sys
from datetime import date
from pathlib import Path
from typing import Callable, TypedDict

import toml

from m23.constants import (
    CAMERA_CHANGE_2022_DATE,
    INPUT_CALIBRATION_FOLDER_NAME,
    TYPICAL_NEW_CAMERA_CROP_REGION,
)
from m23.processor.config_loader import (
    ConfigImage,
    is_night_name_valid,
    prompt_to_continue,
)
from m23.utils import get_date_from_input_night_folder_name, get_flats


class MasterflatGeneratorConfig(TypedDict):
    input: Path | str
    output: Path | str
    image: ConfigImage


def is_valid(config: MasterflatGeneratorConfig) -> bool:
    """
    Returns whether the configuration file is valid
    """
    NIGHT_INPUT_PATH = Path(config["input"])
    if not NIGHT_INPUT_PATH.exists():
        sys.stderr.write(f"Input folder {NIGHT_INPUT_PATH} doesn't exist.\n")
        return False

    # Verify that the Night folder name matches the naming convention
    if not is_night_name_valid(NIGHT_INPUT_PATH):
        return False

    # Verify that the CALIBRATION FOLDER exists
    CALIBRATION_FOLDER_PATH = NIGHT_INPUT_PATH / INPUT_CALIBRATION_FOLDER_NAME
    if not CALIBRATION_FOLDER_PATH.exists():
        sys.stderr.write(f"Calibration folder {CALIBRATION_FOLDER_PATH} doesn't exist.\n")
        return False

    # Verify that the night contains flats to use
    if len(list(get_flats(CALIBRATION_FOLDER_PATH))) == 0:
        sys.stderr.write(
            f"Night {NIGHT_INPUT_PATH} doesn't contain flats in {CALIBRATION_FOLDER_PATH}. Provide masterflat path.\n"
        )
        return False

    try:
        output_path = Path(config["output"])
        output_path.mkdir(parents=True, exist_ok=True)  # Create directory if not exists
    except Exception as e:
        sys.stderr.write(f"Error in output folder. {e} \n")
        return False

    if not is_image_properties_valid(config["image"]):
        return False


def is_image_properties_valid(image_config: ConfigImage) -> bool:
    """
    Checks and returns if  the image_properties is valid.
    If invalid, write the error msg in stderr.
    """

    # Validate the image properties in the configuration file
    # Ensure that rows and cols are int > 0
    rows, cols = image_config["rows"], image_config["columns"]
    if type(rows) != int or type(cols) != int or rows <= 0 or cols <= 0:
        sys.stderr.write(
            f"Rows and columns of image have to be > 0. Got  rows:{rows} cols:{cols}\n"
        )
        return False
    # Ensure that if crop_region is present, it has to be list of list of ints
    if crop_region := image_config.get("crop_region"):
        try:
            for i in crop_region:
                for j in i:
                    if type(j) != int or j <= 0:
                        sys.stderr.write(f"Invalid value detected in crop_region {j}.\n")
                        return False
        except Exception as e:
            return False

    return True  # No error detected


def create_enhanced_config(config: MasterflatGeneratorConfig) -> MasterflatGeneratorConfig:
    """
    This function enhances the configuration file for ease of functions
    that later require processing of the config file
    """
    # Covert folder str to path
    config["input_calibration_folder"] = Path(config["input_calibration_folder"])
    config["output_calibration_folder"] = Path(config["output_calibration_folder"])
    return config


def sanity_check_image(config: ConfigImage, night_date: date):
    """
    Checks for abnormal values in configuration images
    """
    rows, cols = config["rows"], config["columns"]
    crop_region = config["image"].get("crop_region")
    old_camera = night_date < CAMERA_CHANGE_2022_DATE
    if old_camera:
        if rows != 1024:
            prompt_to_continue(f"Detected non 1024 image row value for old camera date")
        if cols != 1024:
            prompt_to_continue(f"Detected non 1024 image column value for old camera date")
        if crop_region and type(crop_region) == list and len(crop_region) > 0:
            prompt_to_continue(f"Detected use of crop region for old camera.")
    else:
        if rows != 2048:
            prompt_to_continue(f"Detected non 2048 image row value for new camera date")
        if cols != 2048:
            prompt_to_continue(f"Detected non 2048 image column value for new camera date")
        if (
            not crop_region
            or crop_region
            and type(crop_region) != list
            or type(crop_region) == list
            and len(crop_region) == 0
        ):
            prompt_to_continue(
                f"We typically use crop images from new camera, you don't seem to define it"
            )
            try:
                for crop_section_index, crop_section in enumerate(crop_region):
                    for section_coordinate_index, section_coordinate in enumerate(crop_section):
                        if (
                            section_coordinate
                            != TYPICAL_NEW_CAMERA_CROP_REGION[crop_section_index][
                                section_coordinate_index
                            ]
                        ):
                            prompt_to_continue(
                                f"Mismatch between default crop region used in new camera and config file"
                            )
                            return  # Ignore further checking if already made the user aware of inconsistency once

            except Exception as e:
                prompt_to_continue(
                    f"Error while checking crop region with standard crop region value. {e}"
                )


def sanity_check(config: MasterflatGeneratorConfig) -> MasterflatGeneratorConfig:
    """
    This method is warn about technically correct but abnormal configuration values
    """
    night_date = get_date_from_input_night_folder_name(config["input"])
    sanity_check_image(config["image"], night_date)
    return config


def validate_generate_masterflat_config_file(
    file_path: Path, on_success: Callable[[MasterflatGeneratorConfig], None]
):
    """
    This method reads configuration file for generating masterflat
    and if the config is valid, calls the unary on_success function with the
    configuration file
    """

    if not file_path.exists() or not file_path.exists():
        raise FileNotFoundError("Cannot find configuration file")
    match toml.load(file_path):
        case {
            "input": _,
            "output": _,
            "image": {"rows": int(_), "columns": int(_), **optional_image_options},
        } as masterflat_generator_config if is_valid(masterflat_generator_config):
            on_success(sanity_check(create_enhanced_config(masterflat_generator_config)))
        case _:
            sys.stderr.write("Stopping because the provided configuration file has issues.\n")
