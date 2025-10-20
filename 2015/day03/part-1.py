from utils.io import read_input
from utils.point import DOWN, LEFT, RIGHT, UP, Point

data = read_input()

location = Point(0, 0)
visited_locations = {location}
for x in data:
    match x:
        case "^":
            location += UP
        case "v":
            location += DOWN
        case ">":
            location += RIGHT
        case "<":
            location += LEFT
    visited_locations.add(location)

print(len(visited_locations))
