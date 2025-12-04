from collections.abc import Iterable

from utils.io import read_input_lines

grid = {}


for y, line in enumerate(read_input_lines()):
    for x, spot in enumerate(line):
        grid[(x, y)] = 1 if spot == "@" else 0


def get_neighbors(x: int, y: int) -> Iterable[tuple[int, int]]:
    for neighbor_x in range(x - 1, x + 2):
        for neighbor_y in range(y - 1, y + 2):
            if not (neighbor_x == x and neighbor_y == y):
                yield neighbor_x, neighbor_y


answer = 0
changes = True
while changes:
    changes = False
    for roll in filter(lambda k: grid[k] == 1, grid):
        if sum(grid.get(neighbor, 0) for neighbor in get_neighbors(*roll)) < 4:
            answer += 1
            grid[roll] = 0
            changes = True

print(answer)
