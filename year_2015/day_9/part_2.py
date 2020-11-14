import re
from itertools import permutations


def run(puzzle_input):
    input_regex = r'(?P<city_0>\w*) to (?P<city_1>\w*) = (?P<distance>\d*)'

    # Create data which makes solving the issue easier.
    distances = {}
    stars = set()
    for line in puzzle_input:
        m = re.match(input_regex, line)
        if m:
            data = m.groupdict()
            distances[f'{data["city_0"]}_{data["city_1"]}'] = int(data['distance'])
            distances[f'{data["city_1"]}_{data["city_0"]}'] = int(data['distance'])
            stars.add(data['city_0'])
            stars.add(data['city_1'])

    def find_distance(current_star, next_stars):
        next_star = next_stars[0]
        if len(next_stars) > 1:
            return distances[f'{current_star}_{next_star}'] + find_distance(next_star, next_stars[1:])
        return distances[f'{current_star}_{next_star}']

    return max([find_distance(route[0], route[1:]) for route in permutations(stars)])


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
