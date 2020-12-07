import re
from collections import defaultdict


def run(puzzle_input):
    # Regex
    bag_re = r'(?P<color>\w+ \w+) bags contain (?P<items>.+)'
    item_re = r'(?P<count>\d+) (?P<color>\w+ \w+) bag'

    bags = map(lambda x: re.match(bag_re, x).groupdict(), puzzle_input)

    # Create data
    item_in_bag = defaultdict(list)
    for bag in bags:
        for item in re.finditer(item_re, bag['items']):
            key = item.groupdict()['color']
            value = int(item.groupdict()['count'])
            item_in_bag[bag['color']].append((key, value))

    def count_bags(color):
        return sum(item[1] * (count_bags(item[0]) + 1) if item[0] in item_in_bag else item[1]
                   for item in item_in_bag[color])

    return count_bags('shiny gold')


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
