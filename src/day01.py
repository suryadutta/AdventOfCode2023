from src._logger import LOGGER
from src.utils import get_data

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


def get_calibration_value_from_line(line: str, parse_numeric_words: bool) -> int:
    if parse_numeric_words:
        for num_word in NUMBERS_TEXT:
            line = line.replace(
                num_word, f"{num_word[0]}{NUMBERS_TEXT[num_word]}{num_word[-1]}"
            )

    first_number = int(next(char for char in line if char.isnumeric()))
    last_number = int(next(char for char in reversed(line) if char.isnumeric()))
    return 10 * first_number + last_number


def run_part_a() -> str:
    LOGGER.info("Running code for Part A")

    return str(
        sum(
            get_calibration_value_from_line(line=line, parse_numeric_words=False)
            for line in get_data()
        )
    )


def run_part_b() -> str:
    LOGGER.info("Running code for Part B")

    return str(
        sum(
            get_calibration_value_from_line(line=line, parse_numeric_words=True)
            for line in get_data()
        )
    )
