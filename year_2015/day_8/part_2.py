def run(puzzle_input):
    return sum(2 + literal.count('\\') + literal.count('"') for literal in puzzle_input)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
