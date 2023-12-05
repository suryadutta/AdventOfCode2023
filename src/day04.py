import re
from collections import defaultdict
from dataclasses import dataclass

from src._logger import LOGGER
from src.utils import get_data


@dataclass(frozen=True)
class ScratchCard:
    card_id: int
    winning_numbers: set[int]
    numbers: set[int]

    @property
    def num_winning_cards(self):
        return len(self.winning_numbers.intersection(self.numbers))

    @staticmethod
    def populate_from_line(line: str) -> "ScratchCard":
        split1 = line.split("|")
        split2 = split1[0].split(":")

        return ScratchCard(
            card_id=int(re.match("Card\s+(\d+)", split2[0]).group(1)),
            winning_numbers={
                int(num.group()) for num in re.finditer(r"\d+", split2[1])
            },
            numbers={int(num.group()) for num in re.finditer(r"\d+", split1[1])},
        )


def run_part_a() -> str:
    LOGGER.info("Running code for Part A")

    data = get_data()

    total_points = 0
    for line in data:
        card = ScratchCard.populate_from_line(line=line)
        if card.num_winning_cards > 0:
            total_points += 2 ** (card.num_winning_cards - 1)

    return str(total_points)


def run_part_b() -> str:
    LOGGER.info("Running code for Part B")

    card_counts: defaultdict[int, int] = defaultdict(lambda: 0)

    data = get_data()
    for line in data:
        card = ScratchCard.populate_from_line(line=line)
        card_counts[card.card_id] = card_counts[card.card_id] + 1

        if card.num_winning_cards > 0:
            for i in range(1, card.num_winning_cards + 1):
                card_counts[card.card_id + i] += card_counts[card.card_id]

    return str(sum(card_counts.values()))
