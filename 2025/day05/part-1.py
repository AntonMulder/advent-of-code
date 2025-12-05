from utils.io import read_input as read_data

ingredient_ranges, product_ids = (x.split("\n") for x in read_data().split("\n\n"))

answer = sum(
    any(
        start <= product_id <= stop
        for start, stop in (
            map(int, ingredient_range.split("-"))
            for ingredient_range in ingredient_ranges
        )
    )
    for product_id in map(int, product_ids)
)

print(answer)
