from utils.io import read_input as read_data

raw_ingredient_ranges, _ = (x.split("\n") for x in read_data().split("\n\n"))

ingredient_ranges = sorted(
    [int(x) for x in raw_ingredient_range.split("-")]
    for raw_ingredient_range in raw_ingredient_ranges
)

answer = 0
start, end = ingredient_ranges.pop(0)
for ingredient_range in ingredient_ranges:
    range_start, range_end = ingredient_range

    if range_start <= end:
        end = max(end, range_end)
    else:
        answer += end - start + 1
        start = range_start
        end = range_end
answer += end - start + 1

print(answer)
