import re
from collections import defaultdict

from utils.io import read_input_lines

data = read_input_lines()


def get_distance(speed: int, flying: int, resting: int, elapsed_seconds: int) -> int:
    total_time = flying + resting
    complete_rounds = int(elapsed_seconds / total_time)
    remaining_round = min(elapsed_seconds % total_time, flying)
    return complete_rounds * speed * flying + (remaining_round * speed)


reindeer = {}
for x in data:
    name, speed, flying, resting = re.match(
        r"(\w+) can fly (\d+) km/s for (\d+) seconds, but "
        r"then must rest for (\d+) seconds.",
        x,
    ).groups()

    reindeer[name] = {
        "speed": int(speed),
        "flying": int(flying),
        "resting": int(resting),
    }


points = defaultdict(int)
for second in range(1, 2503):
    distances = {}
    for name, reindeer_info in reindeer.items():
        distances[name] = get_distance(
            elapsed_seconds=second,
            **reindeer_info,
        )

    max_distance = max(distances.values())

    for name, distance in distances.items():
        if distance == max_distance:
            points[name] += 1

print(max(points.values()))
