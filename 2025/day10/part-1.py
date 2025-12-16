import re
from collections import deque

from utils.io import read_input_lines as read_data

answer = 0
for data in read_data():
    indicator_light, buttons = re.match(r"^\[(.+)\] (.+) .+$", data).groups()

    final_state = tuple(light == "#" for light in indicator_light)
    button_set = [
        tuple(int(y) for y in re.findall(r"\d", x)) for x in buttons.split(" ")
    ]

    initial_state = tuple(False for _ in indicator_light)
    queue = deque([(0, initial_state)])
    visited = {initial_state}

    while queue:
        presses, light = queue.popleft()

        if light == final_state:
            answer += presses
            break

        for button in button_set:
            new_light = list(light)
            for idx in button:
                new_light[idx] = not new_light[idx]
            new_light = tuple(new_light)

            if new_light not in visited:
                visited.add(new_light)
                queue.append((presses + 1, new_light))

print(answer)
