from unittest.mock import patch

from src.day07 import run_part_a, run_part_b

TEST_LINES = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


@patch("src.day07.get_data")
def test_run_part_a(mock_get_data):
    mock_get_data.return_value = TEST_LINES
    assert run_part_a() == str(6440)


@patch("src.day07.get_data")
def test_run_part_b(mock_get_data):
    mock_get_data.return_value = TEST_LINES
    assert run_part_b() == str(71503)
