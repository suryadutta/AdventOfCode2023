from unittest.mock import patch

from src.day03 import (
    Location,
    run_part_a,
    run_part_b,
    yield_part_number_adjacent_locations,
)

TEST_LINES = [
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


def test_yield_part_number_adjacent_locations():
    test_line = "467..114.."
    test_row_num = 1

    exp_adjacent_rows = [0, 1, 2]

    exp_adjacent_cols_467 = [0, 1, 2, 3]
    exp_adjacent_cols_114 = [4, 5, 6, 7, 8]

    all_part_numbers_adjacent_locations = list(
        yield_part_number_adjacent_locations(line=test_line, row_num=test_row_num)
    )

    adjacent_locations_467 = list(
        filter(lambda x: x[0] == 467, all_part_numbers_adjacent_locations)
    )
    for exp_col in exp_adjacent_cols_467:
        for exp_row in exp_adjacent_rows:
            assert (467, Location(row=exp_row, col=exp_col)) in adjacent_locations_467
    assert len(adjacent_locations_467) == len(exp_adjacent_cols_467) * len(
        exp_adjacent_rows
    )

    adjacent_locations_114 = list(
        filter(lambda x: x[0] == 114, all_part_numbers_adjacent_locations)
    )
    for exp_col in exp_adjacent_cols_114:
        for exp_row in exp_adjacent_rows:
            assert (114, Location(row=exp_row, col=exp_col)) in adjacent_locations_114
    assert len(adjacent_locations_114) == len(exp_adjacent_cols_114) * len(
        exp_adjacent_rows
    )


@patch("src.day03.get_data")
def test_run_part_a(mock_get_data):
    mock_get_data.return_value = TEST_LINES
    assert run_part_a() == str(4361)


@patch("src.day03.get_data")
def test_run_part_b(mock_get_data):
    mock_get_data.return_value = TEST_LINES
    assert run_part_b() == str(467835)
