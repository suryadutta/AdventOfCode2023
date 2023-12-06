import math
import re

from src._logger import LOGGER
from src.utils import get_data


def run_part_a() -> str:
    LOGGER.info("Running code for Part A")

    data = get_data()

    times = [int(num.group()) for num in re.finditer(r"\d+", data[0])]
    record_distances = [int(num.group()) for num in re.finditer(r"\d+", data[1])]

    # brute force
    ways_to_beat_all_races = []
    for time, record_distance in zip(times, record_distances, strict=True):
        ways_to_beat = 0
        for hold_duration in range(1, time):
            travel_duration = time - hold_duration
            distance = travel_duration * hold_duration
            if distance > record_distance:
                ways_to_beat += 1
        ways_to_beat_all_races.append(ways_to_beat)

    return str(math.prod(ways_to_beat_all_races))


def run_part_b() -> str:
    LOGGER.info("Running code for Part B")

    data = get_data()
    time = int(data[0].split(":")[1].strip().replace(" ", ""))
    distance = int(data[1].split(":")[1].strip().replace(" ", ""))

    # to find the hold times that equal the record distance,
    # can convert to a polynomial function:
    #
    # time = hold_time + travel_time
    # hold_time = speed
    # distance = travel_time * speed
    #          = (time - hold_time) * hold_time
    #          = -hold_time**2 + time * hold_time
    #
    # using the good ol quadratic formula, where
    #    a = -1
    #    b = time
    #    c = -1 * record distance
    # we get the two hold times that equal the record distance,
    # so all integer hold times between this beat the record distance

    import numpy as np

    min_root = (-1 * time + np.sqrt(np.square(time) - 4 * (-1) * (-1 * distance))) / (
        2 * -1
    )
    max_root = (-1 * time - np.sqrt(np.square(time) - 4 * (-1) * (-1 * distance))) / (
        2 * -1
    )

    num_ways_to_win = int(np.floor(max_root) - np.ceil(min_root)) + 1
    return str(num_ways_to_win)
