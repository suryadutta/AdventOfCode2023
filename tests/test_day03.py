from unittest.mock import patch

from src.day03 import (
    run_part_a,
    run_part_b,
)


@patch("src.day03.get_data")
def test_run_part_a(mock_get_data):
    mock_get_data.return_value = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]

    answer = run_part_a()
    assert answer == str(4361)


@patch("src.day03.get_data")
def test_run_part_b(mock_get_data):
    mock_get_data.return_value = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]

    answer = run_part_b()
    assert answer == str(467835)
