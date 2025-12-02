import re

from utils.io import read_input

product_id_ranges = read_input().split(",")

answer = 0
for product_id_range in product_id_ranges:
    start, end = product_id_range.split("-")

    answer += sum(
        product_id
        for product_id in range(int(start), int(end) + 1)
        if re.match(r"^(?!0)(\d+)\1$", str(product_id))
    )

print(answer)
