from unittest.mock import patch

import pytest

from src.day07 import CardHand, CardHandType, run_part_a, run_part_b

TEST_LINES = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


@pytest.mark.parametrize(
    "input_hand, expected",
    [
        (["2", "3", "4", "5", "6"], CardHandType.HIGH_CARD),
        (["2", "3", "4", "6", "6"], CardHandType.ONE_PAIR),
        (["2", "4", "4", "6", "6"], CardHandType.TWO_PAIR),
        (["2", "4", "6", "6", "6"], CardHandType.THREE_OF_A_KIND),
        (["2", "2", "6", "6", "6"], CardHandType.FULL_HOUSE),
        (["2", "6", "6", "6", "6"], CardHandType.FOUR_OF_A_KIND),
        (["6", "6", "6", "6", "6"], CardHandType.FIVE_OF_A_KIND),
    ],
)
def test_card_hand_type(input_hand: list[str], expected: CardHandType):
    card_hand = CardHand(cards=input_hand, bid=10)
    assert card_hand.hand_type == expected


@pytest.mark.parametrize(
    "input_hand, expected",
    [
        (
            ["2", "3", "4", "5", "6"],
            1 * (14**5) + 1 * (14**4) + 2 * (14**3) + 3 * (14**2) + 4 * (14**1) + 5,
        ),
        (
            ["6", "6", "6", "6", "6"],
            7 * (14**5) + 5 * (14**4) + 5 * (14**3) + 5 * (14**2) + 5 * (14**1) + 5,
        ),
    ],
)
def test_card_hand_score(input_hand: list[str], expected: int):
    card_hand = CardHand(cards=input_hand, bid=10)
    assert card_hand.score == expected


@patch("src.day07.get_data")
def test_run_part_a(mock_get_data):
    mock_get_data.return_value = TEST_LINES
    assert run_part_a() == str(6440)


@patch("src.day07.get_data")
def test_run_part_b(mock_get_data):
    mock_get_data.return_value = TEST_LINES
    assert run_part_b() == str(71503)
