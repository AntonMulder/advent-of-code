import re


def ingredient_score(amount, capacity, durability, flavor, texture, calories):
    return amount * capacity + amount * durability + amount * flavor + amount * texture


def run(puzzle_input):
    ingredient_regex = re.compile(r'(?P<name>\w+): capacity (?P<capacity>-?\d+), durability (?P<durability>-?\d+), '
                                  r'flavor (?P<flavor>-?\d+), texture (?P<texture>-?\d+), '
                                  r'calories (?P<calories>-?\d+)')
    return ingredient_regex


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
