from itertools import combinations


def run(puzzle_input):
    numbers = list(map(int, puzzle_input))

    index = slice_size = 25
    while True:
        value = numbers[index]
        preamble = set(map(lambda x: sum(x), combinations(numbers[index - slice_size: index], r=2)))

        if value not in preamble:
            break

        index += 1
    return value


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
