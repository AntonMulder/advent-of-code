import re

from utils.io import read_input

data = read_input()

for x in range(50):
    data = re.sub(r"(\d)\1*", lambda x: f"{len(x[0])}{x[1]}", data)

print(len(data))
