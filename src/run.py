import importlib
import os

from src._logger import LOGGER


def run_code():
    day = int(os.environ["AOC_DAY"])

    try:
        answers_module = importlib.import_module(f"src.day{day:02d}")

        run_part_a = answers_module.run_part_a
        try:
            LOGGER.info(f"Part A Answer: {run_part_a()}")
        except NotImplementedError:
            LOGGER.error("Part A not started yet")

        run_part_b = answers_module.run_part_b
        try:
            LOGGER.info(f"Part B Answer: {run_part_b()}")
        except NotImplementedError:
            LOGGER.error("Part B not started yet")
    except ModuleNotFoundError:
        LOGGER.error(f"src/day{day:02d}.py not found")


if __name__ == "__main__":
    run_code()
