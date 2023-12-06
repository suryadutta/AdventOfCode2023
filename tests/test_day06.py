from unittest.mock import patch

from src.day06 import run_part_a, run_part_b

TEST_LINES = ["Time:      7  15   30", "Distance:  9  40  200"]


@patch("src.day06.get_data")
def test_run_part_a(mock_get_data):
    mock_get_data.return_value = TEST_LINES
    assert run_part_a() == str(288)


@patch("src.day06.get_data")
def test_run_part_b(mock_get_data):
    mock_get_data.return_value = TEST_LINES
    assert run_part_b() == str(71503)
