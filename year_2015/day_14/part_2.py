import re

from year_2015.day_14.utils import get_distance


def run(puzzle_input):
    reindeer_regex = re.compile(r'(?P<name>\w*) can fly (?P<speed>\d*) km\/s for (?P<speed_seconds>\d*) seconds, '
                                r'but then must rest for (?P<rest_seconds>\d*) seconds.')

    reindeers = [re.match(reindeer_regex, reindeer).groupdict() for reindeer in puzzle_input]

    leaderboard = {reindeer['name']: 0 for reindeer in reindeers}

    for time in range(1, 2504):
        reindeer_positions = {reindeer['name']: get_distance(time, **reindeer)for reindeer in reindeers}

        leading_position = max(reindeer_positions.values())
        for name, position in reindeer_positions.items():
            if position == leading_position:
                leaderboard[name] += 1

    return max(leaderboard.values())


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
