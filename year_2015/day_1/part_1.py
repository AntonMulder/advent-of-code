def run(puzzle_input):
    puzzle_input_list = list(puzzle_input)
    return puzzle_input_list.count('(') - puzzle_input_list.count(')')


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read()))
