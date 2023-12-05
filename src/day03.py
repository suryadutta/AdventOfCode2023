import re
from dataclasses import dataclass
from typing import Iterator

from src._logger import LOGGER
from src.utils import get_data


@dataclass(frozen=True)
class Location:
    row: int
    col: int


def yield_part_number_adjacent_locations(
    line: str, row_num: int
) -> Iterator[tuple[int, Location]]:
    for num_match in re.finditer(r"\d+", line):
        for location in {
            Location(row=r, col=c)
            for r in (row_num - 1, row_num, row_num + 1)
            for c in range(num_match.start() - 1, num_match.end() + 1)
        }:
            yield int(num_match.group()), location


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
        part_number
        for row_num, line in enumerate(data)
        for part_number, location in yield_part_number_adjacent_locations(
            line=line, row_num=row_num
        )
        if location in symbols
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

    for row_num, line in enumerate(data):
        for part_number, location in yield_part_number_adjacent_locations(
            line=line, row_num=row_num
        ):
            if location in gear_symbols_and_part_numbers:
                gear_symbols_and_part_numbers[location].append(part_number)

    return str(
        sum(
            [
                part_numbers[0] * part_numbers[1]
                for part_numbers in gear_symbols_and_part_numbers.values()
                if len(part_numbers) == 2
            ]
        )
    )
