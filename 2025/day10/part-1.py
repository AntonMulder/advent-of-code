import copy
import heapq
import re

from utils.io import read_input_lines as read_data

answer = 0
for data in read_data():
    indicator_light, buttons, joltage = re.match(
        r"^\[(.+)\] (.+) (\{.+\})$", data
    ).groups()

    final_state = [True if light == "#" else False for light in indicator_light]

    h = []
    button_set = [[int(y) for y in re.findall(r"\d", x)] for x in buttons.split(" ")]
    for buttons in button_set:
        heapq.heappush(h, (0, [False] * len(indicator_light), buttons))

    while True:
        score, light, buttons = heapq.heappop(h)
        light = copy.copy(light)
        score += 1

        for button in buttons:
            light[button] = not light[button]

        if final_state == light:
            answer += score
            break
        else:
            for buttons in button_set:
                if (score, light, buttons) not in h:
                    heapq.heappush(h, (score, light, buttons))

print(answer)
