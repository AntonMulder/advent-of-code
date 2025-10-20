from __future__ import annotations

from typing import NamedTuple


class Point(NamedTuple):
    y: int
    x: int

    def __add__(self, point: Point) -> Point:
        return Point(self.y + point.y, self.x + point.x)

    def __sub__(self, point: Point) -> Point:
        return Point(self.y - point.y, self.x - point.x)


UP = Point(1, 0)
RIGHT = Point(0, 1)
DOWN = Point(-1, 0)
LEFT = Point(0, -1)
