import re
from dataclasses import dataclass

from src._logger import LOGGER
from src.utils import get_data


@dataclass(frozen=True)
class Location:
    row: int
    col: int


def run_part_a() -> str:
    LOGGER.info("Running code for Part A")

    data = get_data()

    symbols: set[Location] = {
        Location(row=r, col=c)
        for r in range(len(data))
        for c in range(len(data[0]))
        if data[r][c] not in "0123456789."
    }

    part_numbers = [
        int(num_match.group())
        for r, line in enumerate(data)
        for num_match in re.finditer(r"\d+", line)
        for _location in {
            Location(row=r, col=c)
            for r in (r - 1, r, r + 1)
            for c in range(num_match.start() - 1, num_match.end() + 1)
        }
        & symbols
    ]

    return str(sum(part_numbers))


def run_part_b() -> str:
    LOGGER.info("Running code for Part B")

    data = get_data()

    gear_symbols_and_part_numbers: dict[Location, list[int]] = {
        Location(row=r, col=c): []
        for r in range(len(data))
        for c in range(len(data[0]))
        if data[r][c] == "*"
    }

    for r, line in enumerate(data):
        for num_match in re.finditer(r"\d+", line):
            for location in {
                Location(row=r, col=c)
                for r in (r - 1, r, r + 1)
                for c in range(num_match.start() - 1, num_match.end() + 1)
            } & gear_symbols_and_part_numbers.keys():
                gear_symbols_and_part_numbers[location].append(int(num_match.group()))

    return str(
        sum(
            [
                part_numbers[0] * part_numbers[1]
                for part_numbers in gear_symbols_and_part_numbers.values()
                if len(part_numbers) == 2
            ]
        )
    )
