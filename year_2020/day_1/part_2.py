from functools import reduce
from itertools import combinations


def run(puzzle_input):
    match = list(filter(lambda x: sum(x) == 2020, combinations(puzzle_input, r=3)))[0]
    return reduce(lambda x, y: x * y, match)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run([int(x) for x in f.read().splitlines()]))
