import re

from utils.io import read_input_lines

data = read_input_lines()


def contains_pair_twice(text: str) -> bool:
    return bool(re.search(r"(..).*\1", text))


def contains_repeated_letter(text: str) -> bool:
    return bool(re.search(r"(.).\1", text))


print(
    sum(
        1
        for _ in filter(
            contains_pair_twice,
            filter(contains_repeated_letter, data),
        )
    )
)
