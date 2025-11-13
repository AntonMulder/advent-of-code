from functools import reduce
from itertools import combinations
from operator import mul

from utils.io import read_input_lines

packages = [int(x) for x in read_input_lines()]

GROUP_WEIGHT = sum(packages) // 4

items = 1
while not (
    possible_combinations := [
        reduce(mul, combination)
        for combination in combinations(packages, items)
        if sum(combination) == GROUP_WEIGHT
    ]
):
    items += 1

print(min(possible_combinations))
