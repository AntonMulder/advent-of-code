import re
from collections import defaultdict

from utils.io import read_input_lines

data = read_input_lines()

lights = defaultdict(int)
for instruction in data:
    action, top_left_x, top_left_y, bottom_right_x, bottom_right_y = re.match(
        r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)",
        instruction,
    ).groups()

    changes = (
        (x, y)
        for x in range(int(top_left_x), int(bottom_right_x) + 1)
        for y in range(int(top_left_y), int(bottom_right_y) + 1)
    )

    match action:
        case "turn on":
            for change in changes:
                lights[change] += 1
        case "turn off":
            for change in changes:
                lights[change] -= 1 if lights[change] > 0 else 0
        case "toggle":
            for change in changes:
                lights[change] += 2

print(sum(lights.values()))
