import re


def run(puzzle_input):
    sequence_regex = re.compile(r'(\d)\1*')
    for _ in range(40):
        puzzle_input = ''.join([f'{len(m.group())}{m.group()[0]}' for m in re.finditer(sequence_regex, puzzle_input)])

    return len(puzzle_input)


if __name__ == '__main__':
    print(run('1321131112'))
