from collections import defaultdict
from collections.abc import Iterable

from utils.io import read_input_lines

data = read_input_lines()
CORNER_POINT = len(data[0]) - 1
grid = defaultdict(bool)


for y, line in enumerate(data):
    for x, light in enumerate(line):
        grid[(x, y)] = True if light == "#" else False


def get_neighbors(x: int, y: int) -> Iterable[tuple[int, int]]:
    for neighbor_x in range(x - 1, x + 2):
        for neighbor_y in range(y - 1, y + 2):
            if not (neighbor_x == x and neighbor_y == y):
                yield neighbor_x, neighbor_y


for _ in range(100):
    new_grid = defaultdict(bool)
    for light in grid:
        if light in {
            (0, 0),
            (0, CORNER_POINT),
            (CORNER_POINT, 0),
            (CORNER_POINT, CORNER_POINT),
        }:
            new_grid[light] = True
        else:
            neighbor_lights = sum(
                grid.get((x, y), False) for x, y in get_neighbors(*light)
            )
            if grid.get(light):
                new_grid[light] = True if neighbor_lights in {2, 3} else False
            else:
                new_grid[light] = True if neighbor_lights == 3 else False
    grid = new_grid

print(sum(grid.values()))
