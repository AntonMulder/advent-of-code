from itertools import combinations

from utils.io import read_input_lines as read_data

data = [[int(y) for y in x.split(",")] for x in read_data()]

size = 0
for combination in combinations(data, 2):
    width = abs(combination[0][0] - combination[1][0]) + 1
    height = abs(combination[0][1] - combination[1][1]) + 1

    size = max(size, width * height)

print(size)
