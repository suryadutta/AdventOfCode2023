import importlib
import os
import sys

from aocd import submit

from src._logger import LOGGER

DAY = int(os.environ["AOC_DAY"])
YEAR = 2023


def submit_part_a():
    answers_module = importlib.import_module(f"src.day{DAY:02d}")
    run_part_a = answers_module.run_part_a
    submit(run_part_a(), part="a", day=DAY, year=YEAR)
    LOGGER.info("Part A submitted successfully")


def submit_part_b():
    answers_module = importlib.import_module(f"day{DAY:02d}")
    run_part_b = answers_module.run_part_b
    submit(run_part_b(), part="b", day=DAY, year=YEAR)
    LOGGER.info("Part B submitted successfully")


if __name__ == "__main__":
    part = sys.argv[1]

    match part.lower():
        case "a":
            submit_part_a()
        case "b":
            submit_part_b()
        case other:
            raise RuntimeError(f"Invalid part argument: {part}")
