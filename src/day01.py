import re

from src._logger import LOGGER
from src.utils import get_data


def get_calibration_value_from_line(line: str):
    first_number = int(next(char for char in line if char.isnumeric()))
    last_number = int(next(char for char in reversed(line) if char.isnumeric()))
    return 10 * first_number + last_number


NUMBERS_TEXT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_calibration_value_from_line_with_numeric_words(line: str):
    all_numeric_matches = re.findall(
        "(" + "|".join(NUMBERS_TEXT.keys()) + r"|\d{1})", line
    )

    first_number = (
        int(all_numeric_matches[0])
        if all_numeric_matches[0].isnumeric()
        else NUMBERS_TEXT[all_numeric_matches[0]]
    )

    last_number = (
        int(all_numeric_matches[-1])
        if all_numeric_matches[-1].isnumeric()
        else NUMBERS_TEXT[all_numeric_matches[-1]]
    )

    return 10 * first_number + last_number


def run_part_a() -> str:
    LOGGER.info("Running code for Part A")

    return str(sum(get_calibration_value_from_line(line=line) for line in get_data()))


def run_part_b() -> str:
    LOGGER.info("Running code for Part B")

    return str(
        sum(
            get_calibration_value_from_line_with_numeric_words(line=line)
            for line in get_data()
        )
    )
