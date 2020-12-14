import math
import re


def run(puzzle_input):
    timestamp = int(puzzle_input[0])

    bus_ids = [int(x.group()) for x in re.finditer(r'\d+', puzzle_input[1])]

    bus_times = map(lambda x: x * math.ceil(timestamp / x), bus_ids)

    differences = {bus_id: time - timestamp for bus_id, time in zip(bus_ids, bus_times)}

    bus_id = min(differences.keys(), key=(lambda x: differences[x]))

    return differences[bus_id] * bus_id


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
