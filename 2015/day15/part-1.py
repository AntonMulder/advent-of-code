import re

from utils.io import read_input_lines

ingredients = {}
for x in read_input_lines():
    ingredient, capacity, durability, flavor, texture = re.match(
        r"(.+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), "
        r"texture (-?\d+), calories .+",
        x,
    ).groups()
    ingredients[ingredient] = [int(x) for x in (capacity, durability, flavor, texture)]


def score(teaspoons: list[int]) -> int:
    score = 1
    ing = list(ingredients.values())
    for i in range(len(ing[0])):
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
