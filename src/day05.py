import re
from dataclasses import dataclass

from src._logger import LOGGER
from src.utils import get_data


@dataclass
class Rule:
    destination_range_start: int
    source_range_start: int
    range_length: int

    @property
    def offset(self):
        return self.destination_range_start - self.source_range_start

    def value_in_range(self, value: int) -> bool:
        return (
            self.source_range_start
            <= value
            <= self.source_range_start + self.range_length - 1
        )

    def map_value(self, value: int) -> int:
        return value + self.offset

    @staticmethod
    def map_value_with_rules(value: int, rules: list["Rule"]) -> int:
        for rule in rules:
            if rule.value_in_range(value):
                return rule.map_value(value)
        return value

    @staticmethod
    def parse_from_line(rule_line: str) -> "Rule":
        rule_values = rule_line.strip().split(" ")
        return Rule(
            destination_range_start=int(rule_values[0]),
            source_range_start=int(rule_values[1]),
            range_length=int(rule_values[2]),
        )


def run_part_a() -> str:
    LOGGER.info("Running code for Part A")

    lines = get_data()

    mapped_values = [
        int(num.group()) for num in re.finditer(r"\d+", lines[0].split(":")[1])
    ]

    delimiters = [i for i in range(len(lines)) if lines[i] == ""]
    for delimiter_index in range(0, len(delimiters)):
        rules_start_index = delimiters[delimiter_index] + 2
        if delimiter_index < len(delimiters) - 1:
            rules_end_index = delimiters[delimiter_index + 1]
            rules_lines = lines[rules_start_index:rules_end_index]
        else:
            rules_lines = lines[rules_start_index:]

        rules = [Rule.parse_from_line(line) for line in rules_lines]
        mapped_values = [
            Rule.map_value_with_rules(value=value, rules=rules)
            for value in mapped_values
        ]

    return str(min(mapped_values))


def run_part_b() -> str:
    LOGGER.info("Running code for Part B")
    raise NotImplementedError
