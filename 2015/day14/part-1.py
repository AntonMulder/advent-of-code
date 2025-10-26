import re

from utils.io import read_input_lines

data = read_input_lines()

TIME = 2503


def get_distance(speed: int, flying: int, resting: int) -> int:
    total_time = flying + resting
    complete_rounds = int(TIME / total_time)
    remaining_round = min(TIME % total_time, flying)
    return complete_rounds * speed * flying + (remaining_round * speed)


distance = 0
for x in data:
    speed, flying, resting = re.match(
        r".+ fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",
        x,
    ).groups()

    distance = max(get_distance(int(speed), int(flying), int(resting)), distance)
print(distance)
