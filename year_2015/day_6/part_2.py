import re

import numpy as np


def run(puzzle_input):
    lights = np.zeros((1000, 1000))
    instruction_re = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')

    for instruction in puzzle_input:
        match = instruction_re.match(instruction)

        if match:
            action, x_0, y_0, x_1, y_1 = match.groups()
            if action == 'turn on':
                lights[int(x_0):int(x_1) + 1, int(y_0):int(y_1) + 1] += 1
            elif action == 'turn off':
                subset = lights[int(x_0):int(x_1) + 1, int(y_0):int(y_1) + 1]
                subset[subset > 0] -= 1
            elif action == 'toggle':
                lights[int(x_0):int(x_1) + 1, int(y_0):int(y_1) + 1] += 2

    return np.sum(lights)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
