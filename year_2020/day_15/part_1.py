def run(puzzle_input):
    # Set initial data
    spoken_numbers = {number: turn + 1 for turn, number in enumerate(puzzle_input)}
    last_number = puzzle_input.pop(-1)
    for turn in range(len(spoken_numbers), 2020):
        spoken_numbers[last_number], last_number = turn, turn - spoken_numbers.get(last_number, turn)

    return last_number


if __name__ == '__main__':
    print(run([1, 17, 0, 10, 18, 11, 6]))
