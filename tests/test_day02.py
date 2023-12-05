from unittest.mock import patch

import pytest

from src.day02 import (
    GameInfo,
    parse_game_info,
    run_part_a,
    run_part_b,
)

TEST_LINES = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


@pytest.mark.parametrize(
    "line_input,expected",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            GameInfo(game_id=1, max_green_cubes=2, max_blue_cubes=6, max_red_cubes=4),
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            GameInfo(game_id=2, max_green_cubes=3, max_blue_cubes=4, max_red_cubes=1),
        ),
    ],
)
def test_parse_game_info(line_input: str, expected: GameInfo):
    assert parse_game_info(line_input) == expected


@patch("src.day02.get_data")
def test_run_part_a(mock_get_data):
    mock_get_data.return_value = TEST_LINES
    assert run_part_a() == str(8)


@patch("src.day02.get_data")
def test_run_part_b(mock_get_data):
    mock_get_data.return_value = TEST_LINES
    assert run_part_b() == str(2286)
