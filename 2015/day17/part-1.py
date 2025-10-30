from itertools import combinations

from utils.io import read_input_lines

data = [int(x) for x in read_input_lines()]


def get_combination(data: list[int]):
    for n in range(1, len(data) + 1):
        yield from combinations(data, n)


matches = sum(
    1 for _ in filter(lambda x: sum(x) == 150, (x for x in get_combination(data)))
)

print(matches)
