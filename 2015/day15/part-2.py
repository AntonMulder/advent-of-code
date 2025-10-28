import re

from utils.io import read_input_lines

ingredients = {}
for x in read_input_lines():
    ingredient, capacity, durability, flavor, texture, calories = re.match(
        r"(.+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), "
        r"texture (-?\d+), calories (-?\d+)",
        x,
    ).groups()
    ingredients[ingredient] = [
        int(x) for x in (capacity, durability, flavor, texture, calories)
    ]


def score(teaspoons: list[int]) -> int:
    score = 1
    ing = list(ingredients.values())

    calories = sum(ing[y][4] * teaspoons[y] for y in range(len(ingredients)))
    if calories != 500:
        return 0

    for i in range(len(ing[0]) - 1):
        x = sum(ing[y][i] * teaspoons[y] for y in range(len(ingredients)))
        if x <= 0:
            return 0
        score *= x
    return score


def teaspoons(n, total=100):
    start = total if n == 1 else 0

    for i in range(start, total + 1):
        if n - 1:
            for y in teaspoons(n - 1, total - i):
                yield [i] + y
        else:
            yield [i]


print(max(score(x) for x in teaspoons(len(ingredients))))
