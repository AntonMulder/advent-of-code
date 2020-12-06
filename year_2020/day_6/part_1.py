def run(puzzle_input):
    cleaned_puzzle_input = map(lambda x: x.replace('\n', ''), puzzle_input)

    unique_answers = map(lambda x: len(set(x)), cleaned_puzzle_input)

    return sum(unique_answers)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().split('\n\n')))
