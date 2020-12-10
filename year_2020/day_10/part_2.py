from collections import Counter


def run(puzzle_input):
    puzzle_data = map(lambda x: int(x), puzzle_input)

    sorted_adapters = sorted(puzzle_data)

    counter = Counter((0,))
    for adapter in sorted_adapters:
        counter[adapter] = sum(counter[x] for x in range(adapter - 3, adapter))
    return counter[max(sorted_adapters)]


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
