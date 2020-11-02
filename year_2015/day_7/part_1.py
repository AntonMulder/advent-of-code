import copy
import re


def run(puzzle_input):
    set_value = re.compile(r'(.*) -> (.*)')
    bitwise_operator = re.compile(r'(.*) (AND|OR|LSHIFT|RSHIFT) (.*) -> (.*)')
    bitwise_complement = re.compile(r'NOT (.*) -> (.*)')

    memory = {}

    while len(puzzle_input) > 0:
        new_puzzle_input = copy.deepcopy(puzzle_input)

        for instruction in new_puzzle_input:
            try:
                # Check for bitwise operator.
                match = bitwise_operator.match(instruction)
                if match:
                    left, operator, right, address = match.groups()
                    if operator == 'AND':
                        try:
                            left = int(left)
                            memory[address] = left & memory[right]
                        except Exception:
                            memory[address] = memory[left] & memory[right]
                    elif operator == 'OR':
                        memory[address] = memory[left] | memory[right]
                    elif operator == 'LSHIFT':
                        memory[address] = memory[left] << int(right)
                    elif operator == 'RSHIFT':
                        memory[address] = memory[left] >> int(right)
                else:
                    # Check for bitwise complement.
                    match = bitwise_complement.match(instruction)
                    if match:
                        value_address, address = match.groups()
                        memory[address] = ~memory[value_address]
                    else:
                        # Check for set value.
                        match = set_value.match(instruction)
                        if match:
                            value, address = match.groups()

                            try:
                                memory[address] = int(value)
                            except ValueError:
                                if value in memory.keys():
                                    memory[address] = memory[value]
                                else:
                                    raise KeyError
            except KeyError:
                pass
            else:
                puzzle_input.remove(instruction)
    return memory['a']


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines())['a'])
