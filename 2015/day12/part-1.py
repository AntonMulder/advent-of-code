import re

from utils.io import read_input

data = read_input()

print(sum(int(x) for x in re.findall(r"-?\d+", data)))
