import re
from datetime import date
from pathlib import Path

import numpy as np
import numpy.typing as npt

from m23.constants import FLUX_LOG_COMBINED_FILENAME_DATE_FORMAT


class FluxLogCombinedFile:
    """
    This class is instantiated with the string representing
    file path for the Flux Log Combined file that you want to analyze
    """

    # Class attributes
    header_rows = 6  # Specifies the first x rows that don't contain header information
    file_name_re = re.compile("(\d{2}-\d{2}-\d{2})_m23_7.0-ref_revised_71_(\d{4})_flux.txt")

    def __init__(self, path: str | Path) -> None:
        if type(path) == str:
            path = Path(path)
        self.__path = path
        self.__data = None
        self.__read_data = False
        self.__attendance = None

    @classmethod
    def generate_file_name(cls, night_date: date, star_no: int):
        """
        Returns the file name to use for a given star night for the given night date
        """
        return f"{night_date.strftime(FLUX_LOG_COMBINED_FILENAME_DATE_FORMAT)}_m23_7.0-ref_revised_71_{star_no:04}_flux.txt"

    @property
    def path(self) -> Path:
        return self.__path

    @property
    def attendance(self) -> float | None:
        return self.__attendance

    @property
    def data(self) -> None | npt.ArrayLike:
        """
        The data property returns either None or a numpy one dimensional array
        """
        return self.__data

    def _validate_file(self):
        if not self.path.exists():
            raise FileNotFoundError(f"File not found {self.path}")
        if not self.path.is_file():
            raise ValueError("Directory provided, expected file f{self.path}")

    def _calculate_attendance(self) -> float:
        """
        Calculates and returns the attendance for the night based on `self.data`
        Note that attendance is a value between 0-1.

        Preconditions:
            The object should have valid `self.data`
        Assumptions:
            `self.data` contains all data point albeit empty for a start for the night
        """
        data_points = len(self.data)
        positive_value_data_points = len([x for x in self.data if x > 0])
        return positive_value_data_points / data_points

    def read_file_data(self):
        """
        Reads the file and sets the the data attribute and attendance attribute in the object
        """
        self._validate_file()
        with self.path.open() as fd:
            lines = [line.strip() for line in fd.readlines()]
            lines = lines[self.header_rows :]  # Skip the header rows
            self.__data = np.array(lines, dtype="float")  # Save data as numpy array
        self.__read_data = True  # Marks file as read
        self.__attendance = self._calculate_attendance()

    def is_valid_file_name(self):
        """
        Checks if the file name is valid as per the file naming conventions
        of m23 data processing library. It returns the regex match pattern
        if the file name is valid.
        """
        return self.file_name_re.match(self.path.name)

    def star_number(self) -> int | None:
        """
        Returns the star number associated to the filename if the file name is valid
        """
        if self.is_valid_file_name():
            # The second capture group contains the star number
            return int(self.file_name_re.match(self.path.name)[2])

    def is_file_format_valid(self):
        """
        Checks if the file format is valid
        """
        return True

    def attendance(self) -> float:
        """
        Returns the attendance % (between 0-1) for star for a night
        """
        self._validate_file()
        if not self.__read_data:
            self.read_file_data()
        return self.attendance

    def median(self) -> float:
        """
        Returns the median value for the star for the night
        """
        self._validate_file()
        if not self.__read_data:
            self.read_file_data()
        return np.median(self.data)

    def mean(self) -> float:
        """
        Returns the mean value for the star for the night
        """
        self._validate_file()
        if not self.__read_data:
            self.read_file_data()
        return np.mean(self.data)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"FluxLogCombinedFile {self.path}"
