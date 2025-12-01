import re

from utils.io import read_input_lines

answer = 0
position = 50
for line in read_input_lines():
    direction, distance = re.match(r"([LR])(\d+)", line).groups()
    distance = int(distance)

    if cycles := distance // 100:
        answer += cycles
        distance %= 100

    if direction == "L":
        if distance >= position > 0:
            answer += 1
        position = (position - distance) % 100
    else:
        if distance >= (100 - position) > 0:
            answer += 1
        position = (position + distance) % 100

print(answer)
