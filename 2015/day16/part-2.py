import re

from utils.io import read_input_lines

TICKER_TAPE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def is_sue(sue: str) -> bool:
    (
        id,
        first_property,
        first_value,
        second_property,
        second_value,
        third_property,
        third_value,
    ) = re.match(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", sue).groups()

    def is_valid(property: str, value: int) -> bool:
        if property in ["cats", "trees"]:
            return value > TICKER_TAPE[property]
        elif property in ["pomeranians", "goldfish"]:
            return value < TICKER_TAPE[property]
        else:
            return value == TICKER_TAPE[property]

    return (
        is_valid(first_property, int(first_value))
        and is_valid(second_property, int(second_value))
        and is_valid(third_property, int(third_value))
    )


print(list(filter(lambda x: is_sue(x), read_input_lines())))
