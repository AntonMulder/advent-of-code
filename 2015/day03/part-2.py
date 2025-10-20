from utils.io import read_input
from utils.point import DOWN, LEFT, RIGHT, UP, Point

data = read_input()

santa_location = Point(0, 0)
robot_location = Point(0, 0)
visited_locations = {santa_location}


def new_location(location: Point, x: str) -> Point:
    match x:
        case "^":
            location += UP
        case "v":
            location += DOWN
        case ">":
            location += RIGHT
        case "<":
            location += LEFT
    return location


for i, x in enumerate(data):
    if i % 2 == 0:
        santa_location = new_location(santa_location, x)
        visited_locations.add(santa_location)
    else:
        robot_location = new_location(robot_location, x)
        visited_locations.add(robot_location)

print(len(visited_locations))
