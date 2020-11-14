import re


def run(puzzle_input):
    decimal_number = re.compile(r'-?\d{1,}')
    return sum(int(number) for number in re.findall(decimal_number, puzzle_input))


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read()))
