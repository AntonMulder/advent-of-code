import re
from collections import defaultdict


def run(puzzle_input):
    # Regex
    bag_re = r'(?P<color>\w+ \w+) bags contain (?P<items>.+)'
    item_re = r'[\d+] (?P<color>\w+ \w+) bag'

    bags = map(lambda x: re.match(bag_re, x).groupdict(), puzzle_input)

    # Create data
    item_in_bag = defaultdict(list)
    for bag in bags:
        for item in re.findall(item_re, bag['items']):
            item_in_bag[item].append(bag['color'])

    def find_bags(color):
        for item in item_in_bag[color]:
            bags.add(item)
            if item in item_in_bag:
                find_bags(item)

    # Find bags.
    bags = set()
    find_bags('shiny gold')

    return len(bags)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
