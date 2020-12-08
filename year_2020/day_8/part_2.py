import copy
import re


def run(puzzle_input):
    input_re = r'(?P<operator>\w+) (?P<value>[+-]\d+)'
    matched_input = map(lambda x: re.match(input_re, x).groupdict(), puzzle_input)
    commands = [{'operator': command['operator'], 'value': int(command['value']), 'executed': False}
                for command in matched_input]

    def run_commands(commands):
        index = 0
        accumulator = 0
        while True:
            if index >= len(commands):
                return True, accumulator

            command = commands[index]

            if command['executed']:
                return False, accumulator
            elif command['operator'] == 'acc':
                accumulator += command['value']
                index += 1
            elif command['operator'] == 'jmp':
                index += command['value']
            else:
                index += 1

            command['executed'] = True

    for i in range(0, len(commands)):
        test_commands = copy.deepcopy(commands)
        if test_commands[i]['operator'] == 'jmp':
            test_commands[i]['operator'] = 'nop'
        elif test_commands[i]['operator'] == 'nop':
            test_commands[i]['operator'] = 'jmp'
        result, accumulator = run_commands(test_commands)

        if result:
            return accumulator


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
