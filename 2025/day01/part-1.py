import re

from utils.io import read_input_lines

answer = 0
position = 50
for line in read_input_lines():
    direction, distance = re.match(r"([LR])(\d+)", line).groups()

    if direction == "L":
        position = (position - int(distance)) % 100
    else:
        position = (position + int(distance)) % 100

    if position == 0:
        answer += 1

print(answer)
