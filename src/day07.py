from src._logger import LOGGER
from src.utils import get_data

from collections import Counter
from dataclasses import dataclass

CARDS_BY_STRENGTH = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

@dataclass
class CardHand:
    hand: str

    @property
    def counter(self):
        return Counter(self.hand)

    @property
    def distinct_card_count(self):
        return len(self.counter)

    @property
    def sorted_card_strengths(self):
        strengths = list(map(lambda x: CARDS_BY_STRENGTH.index(x), list(self.counter.keys())))
        strengths.sort(reverse=True)
        return strengths



def run_part_a() -> str:
    LOGGER.info("Running code for Part A")

    hands = []
    bids = []

    for line in get_data():
        split = line.split(" ")

        bid = int(split[1])
        hand = CardHand(hand=split[0])
        strengths = hand.sorted_card_strengths

    return str()


def run_part_b() -> str:
    LOGGER.info("Running code for Part B")
    return str(1)
