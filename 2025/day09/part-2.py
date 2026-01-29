from itertools import combinations

from shapely.geometry import Polygon

from utils.io import read_input_lines as read_data

data = [[int(y) for y in x.split(",")] for x in read_data()]

area = Polygon(data)

rectangles = (
    (min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2))
    for (x1, y1), (x2, y2) in combinations(data, 2)
)

largest_area = 0
for rectangle in rectangles:
    x_min, x_max, y_min, y_max = rectangle
    polygon = Polygon([(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)])

    if polygon.within(area):
        largest_area = max(
            largest_area, (abs(x_min - x_max) + 1) * (abs(y_min - y_max) + 1)
        )

print(largest_area)
