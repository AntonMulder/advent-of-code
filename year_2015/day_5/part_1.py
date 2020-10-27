import re


def run(puzzle_input):
    does_contain = re.compile(r'(ab|cd|pq|xy)')
    appears_twice = re.compile(r'(.)\1')
    three_vowels = re.compile(r'[aeiou]')

    nice = 0
    for string in puzzle_input:
        if (not does_contain.search(string) and
                appears_twice.search(string) and
                len(three_vowels.findall(string)) >= 3):
            nice += 1
    return nice


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
