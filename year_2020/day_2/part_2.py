import re


def run(puzzle_input):
    input_re = r'(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<password>\w+)'

    matches = (re.match(input_re, x) for x in puzzle_input)

    def is_valid(m):
        return (bool(m['password'][int(m['min']) - 1] == m['char']) ^
                bool(m['password'][int(m['max']) - 1] == m['char']))

    valid_passwords = filter(lambda x: is_valid(x), matches)

    return sum(1 for x in valid_passwords)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
