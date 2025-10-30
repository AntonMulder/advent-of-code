import re

from utils.io import read_input_lines

TICKER_TAPE = {
    "children": "3",
    "cats": "7",
    "samoyeds": "2",
    "pomeranians": "3",
    "akitas": "0",
    "vizslas": "0",
    "goldfish": "5",
    "trees": "3",
    "cars": "2",
    "perfumes": "1",
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

    return (
        TICKER_TAPE[first_property] == first_value
        and TICKER_TAPE[second_property] == second_value
        and TICKER_TAPE[third_property] == third_value
    )


print(list(filter(lambda x: is_sue(x), read_input_lines())))
