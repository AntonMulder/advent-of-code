import re

from year_2015.day_14.utils import get_distance


def run(puzzle_input):
    reindeer_regex = re.compile(r'.* can fly (?P<speed>\d*) km\/s for (?P<speed_seconds>\d*) seconds, '
                                r'but then must rest for (?P<rest_seconds>\d*) seconds.')

    time = 2503
    max_distance = 0
    for reindeer in puzzle_input:
        m = re.match(reindeer_regex, reindeer)
        distance = get_distance(time, **m.groupdict())
        max_distance = max(distance, max_distance)

    return max_distance


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
