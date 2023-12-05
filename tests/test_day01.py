from unittest.mock import patch

import pytest

from src.day01 import (
    get_calibration_value_from_line,
    get_calibration_value_from_line_with_numeric_words,
    run_part_a,
    run_part_b,
)


@pytest.mark.parametrize(
    "line,expected",
    [("1abc2", 12), ("pqr3stu8vwx", 38), ("a1b2c3d4e5f", 15), ("treb7uchet", 77)],
)
def test_get_calibration_value_from_line_no_numeric_words(line: str, expected: int):
    assert get_calibration_value_from_line(line=line) == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_get_calibration_value_from_line_with_numeric_words(line: str, expected: int):
    assert get_calibration_value_from_line_with_numeric_words(line=line) == expected


@patch("src.utils.get_data")
def test_run_part_a(mock_get_data, monkeypatch):
    monkeypatch.setenv("AOC_DAY", "1")

    mock_get_data.return_value = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]

    answer = run_part_a()
    assert answer == "142"


@patch("src.utils.get_data")
def test_run_part_b(mock_get_data, monkeypatch):
    monkeypatch.setenv("AOC_DAY", "1")

    mock_get_data.return_value = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]

    answer = run_part_b()
    assert answer == "281"
