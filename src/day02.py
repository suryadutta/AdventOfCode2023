from dataclasses import dataclass

from src._logger import LOGGER
from src.utils import get_data


@dataclass
class GameInfo:
    game_id: int
    max_red_cubes: int
    max_green_cubes: int
    max_blue_cubes: int


def parse_game_info(game_data: str) -> GameInfo:
    max_red_cubes = -1
    max_green_cubes = -1
    max_blue_cubes = -1

    pre_split = game_data.split(":")
    game_id = int(pre_split[0].split(" ")[1])

    for game_round in pre_split[1].split(":"):
        for sub_round in game_round.split(";"):
            for cube_play in sub_round.split(","):
                cube_play_info = cube_play.strip().split(" ")
                color = cube_play_info[1]
                count = int(cube_play_info[0])

                match color:
                    case "red":
                        max_red_cubes = max(max_red_cubes, count)
                    case "green":
                        max_green_cubes = max(max_green_cubes, count)
                    case "blue":
                        max_blue_cubes = max(max_blue_cubes, count)

    return GameInfo(
        game_id=game_id,
        max_red_cubes=max_red_cubes,
        max_green_cubes=max_green_cubes,
        max_blue_cubes=max_blue_cubes,
    )


def run_part_a() -> str:
    LOGGER.info("Running code for Part A")

    total_red_cubes = 12
    total_green_cubes = 13
    total_blue_cubes = 14

    valid_game_ids: set[int] = set()

    for game_data in get_data():
        game_info = parse_game_info(game_data=game_data)

        if (
            game_info.max_red_cubes <= total_red_cubes
            and game_info.max_green_cubes <= total_green_cubes
            and game_info.max_blue_cubes <= total_blue_cubes
        ):
            valid_game_ids.add(game_info.game_id)

    return str(sum(valid_game_ids))


def run_part_b() -> str:
    LOGGER.info("Running code for Part B")

    power_sum = 0

    for game_data in get_data():
        game_info = parse_game_info(game_data=game_data)
        power_sum += (
            game_info.max_red_cubes
            * game_info.max_green_cubes
            * game_info.max_blue_cubes
        )

    return str(power_sum)
