data = open("input").readlines()

ribbon = 0
for present in data:
    length, width, height = (int(x) for x in present.rstrip("\n").split("x"))

    ribbon += min(
        length + length + width + width,
        width + width + height + height,
        height + height + length + length,
    ) + (length * width * height)

print(ribbon)
