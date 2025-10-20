from utils.io import read_input_lines

data = read_input_lines()

wrapping_paper = 0
for present in data:
    length, width, height = (int(x) for x in present.rstrip("\n").split("x"))

    wrapping_paper += (
        2 * length * width
        + 2 * width * height
        + 2 * height * length
        + min(length * width, width * height, height * length)
    )

print(wrapping_paper)
