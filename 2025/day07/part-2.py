from collections import defaultdict

from utils.io import read_input_lines as read_data

manifold = {}
timelines = defaultdict(lambda: 0)

height = 0
for y, line in enumerate(read_data()):
    for x, c in enumerate(line):
        manifold[(y, x)] = c

        if c == "S":
            timelines[x] = 1
    height = y

answer = 0
for y in range(height):
    new_timelines = defaultdict(lambda: 0)

    for x, beams in timelines.items():
        if manifold[(y, x)] == "^":
            new_timelines[x - 1] += beams
            new_timelines[x + 1] += beams
        else:
            new_timelines[x] = beams + new_timelines[x]
    timelines = new_timelines

print(sum(timelines.values()))
