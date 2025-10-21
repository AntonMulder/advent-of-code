from utils.io import read_example_lines

data = read_example_lines()

total = sum(2 + x.count("\\") + x.count('"') for x in data)

print(total)
