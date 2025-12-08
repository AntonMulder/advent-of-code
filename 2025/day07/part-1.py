from utils.io import read_input_lines as read_data

manifold = {}
paths = []
for y, line in enumerate(read_data()):
    for x, c in enumerate(line):
        manifold[(y, x)] = c

        if c == "S":
            paths.append((y, x))

answer = 0
while len(paths):
    y, x = paths.pop(0)

    if (y + 1, x) in manifold:
        if manifold[(y + 1, x)] == "^":
            score = 0
            if (y + 1, x - 1) not in paths:
                score = 1
                paths.append((y + 1, x - 1))
            if (y + 1, x + 1) not in paths:
                score = 1
                paths.append((y + 1, x + 1))
            answer += score
        else:
            paths.append((y + 1, x))

print(answer)
