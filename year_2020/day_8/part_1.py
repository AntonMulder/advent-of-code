import re


def run(puzzle_input):
    input_re = r'(?P<operator>\w+) (?P<value>[+-]\d+)'
    matched_input = map(lambda x: re.match(input_re, x).groupdict(), puzzle_input)
    commands = [{'operator': command['operator'], 'value': int(command['value']), 'executed': False}
                for command in matched_input]

    index = 0
    accumulator = 0
    while True:
        command = commands[index]

        if command['executed']:
            break
        elif command['operator'] == 'acc':
            accumulator += command['value']
            index += 1
        elif command['operator'] == 'jmp':
            index += command['value']
        else:
            index += 1

        command['executed'] = True

    return accumulator


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
