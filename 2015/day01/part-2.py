from utils.io import read_input

data = read_input()

floor = 0
for step, x in enumerate(data, start=1):
    floor += 1 if x == "(" else -1

    if floor == -1:
        print(step)
        break
