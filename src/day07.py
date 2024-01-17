from dataclasses import dataclass
from enum import Enum

from src._logger import LOGGER
from src.utils import get_data

CARDS_BY_STRENGTH = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


class CardHandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


@dataclass
class CardHand:
    cards: list[str]
    bid: int

    @property
    def hand_type(self) -> CardHandType:
        unique_cards = set(self.cards)

        match len(unique_cards):
            case 1:
                return CardHandType.FIVE_OF_A_KIND

            case 2:
                counts = [self.cards.count(value) for value in unique_cards]

                if 4 in counts:
                    return CardHandType.FOUR_OF_A_KIND
                else:
                    return CardHandType.FULL_HOUSE

            case 3:
                counts = [self.cards.count(value) for value in unique_cards]

                # 3 of a kind or 2 pair

                if 3 in counts:
                    return CardHandType.THREE_OF_A_KIND
                else:
                    return CardHandType.TWO_PAIR

            case 4:
                return CardHandType.ONE_PAIR
            case 5:
                return CardHandType.HIGH_CARD

        return CardHandType.HIGH_CARD

    @property
    def score(self) -> int:
        return self.hand_type.value * (14**5) + sum(
            (CARDS_BY_STRENGTH.index(self.cards[i]) + 1) * 14 ** (4 - i)
            for i in range(5)
        )


def run_part_a() -> str:
    LOGGER.info("Running code for Part A")

    hands: list[CardHand] = []

    for line in get_data():
        split = line.split(" ")
        bid = int(split[1])
        cards = list(split[0])
        hands.append(CardHand(cards=cards, bid=bid))

    hands.sort(key=lambda hand: hand.score, reverse=False)
    total_bid_score = sum((rank + 1) * hand.bid for rank, hand in enumerate(hands))
    return str(total_bid_score)


def run_part_b() -> str:
    LOGGER.info("Running code for Part B")
    return str(1)
