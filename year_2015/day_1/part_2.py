def run(puzzle_input):
    puzzle_input_list = list(puzzle_input)
    floor = step = 0
    commands = {'(': 1, ')': -1}

    while floor != -1:
        floor += commands[puzzle_input_list[step]]
        step += 1
    return step


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read()))
