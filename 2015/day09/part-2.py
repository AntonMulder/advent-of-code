import re
from itertools import permutations

from utils.io import read_input_lines

data = read_input_lines()

distances = {}
locations = set()
for x in data:
    start, end, distance = re.match("(.+) to (.+) = (.+)", x).groups()
    distances[(start, end)] = int(distance)
    distances[(end, start)] = int(distance)
    locations.add(start)
    locations.add(end)


def compute_distance(current_location: str, remaining_locations: tuple[str]) -> int:
    distance = distances[(current_location, remaining_locations[0])]
    if len(remaining_locations) > 1:
        return distance + compute_distance(
            remaining_locations[0], remaining_locations[1:]
        )
    return distance


print(max(compute_distance(route[0], route[1:]) for route in permutations(locations)))
