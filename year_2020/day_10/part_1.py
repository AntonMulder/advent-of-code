from collections import Counter
from functools import reduce


def run(puzzle_input):
    puzzle_data = map(lambda x: int(x), puzzle_input)

    sorted_data = sorted(puzzle_data)

    counter = Counter([y - x for x, y in zip(sorted_data[:-1], sorted_data[1:])])

    return reduce(lambda x, y: (x + 1) * (y + 1), counter.values())


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
