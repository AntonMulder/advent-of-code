def run(puzzle_input):
    return sum(len(literal) - len(bytes(literal, 'utf-8').decode('unicode_escape')) + 2 for literal in puzzle_input)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
