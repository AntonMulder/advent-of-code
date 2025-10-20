import re

from utils.io import read_input_lines

data = read_input_lines()


def contains_three_vowels(text: str) -> bool:
    return len(re.findall(r"[aeiou]", text)) >= 3


def contains_double_letter(text: str) -> bool:
    return len(re.findall(r"(.)\1", text)) >= 1


def does_not_contain(text: str) -> bool:
    return not re.search(r"ab|cd|pq|xy", text)


print(
    sum(
        1
        for _ in filter(
            contains_three_vowels,
            filter(
                contains_double_letter,
                filter(does_not_contain, data),
            ),
        )
    )
)
