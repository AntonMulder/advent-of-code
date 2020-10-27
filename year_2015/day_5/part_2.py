import re


def run(puzzle_input):
    contains_pair = re.compile(r'(..).*\1')
    it_repeats = re.compile(r'(.).\1')

    nice = 0
    for string in puzzle_input:
        if it_repeats.search(string) and contains_pair.search(string):
            nice += 1
    return nice


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
