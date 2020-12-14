from functools import reduce


def run(puzzle_input):
    # https://nl.wikipedia.org/wiki/Chinese_reststelling

    bus_times = {int(x): int(x) - i for i, x in enumerate(puzzle_input.split(',')) if x != 'x'}

    product = reduce(lambda x, y: x * y, bus_times.keys())

    total = 0
    for key, value in bus_times.items():
        partial_product = product // key

        inverse = pow(partial_product, -1, key)

        total += value * partial_product * inverse

    return total % product


if __name__ == '__main__':
    with open('data/puzzle_input_2.txt', 'r') as f:
        print(run(f.read()))
