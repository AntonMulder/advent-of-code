def run(puzzle_input):
    def common_answers(answers):
        sets = map(lambda x: set(x), answers.split('\n'))
        return set.intersection(*list(sets))

    cleaned_puzzle_input = map(lambda x: common_answers(x), puzzle_input)

    unique_answers = map(lambda x: len(x), cleaned_puzzle_input)

    return sum(unique_answers)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().split('\n\n')))
