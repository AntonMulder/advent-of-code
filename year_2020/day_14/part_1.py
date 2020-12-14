import re


def run(puzzle_input):
    mask_re = r'mask = (?P<mask>\w+)'
    mem_re = r'mem\[(?P<address>\d+)\] = (?P<value>\d+)'

    memory = {}
    for command in puzzle_input:
        mask = re.match(mask_re, command)

        if mask:
            or_value = int(mask.groupdict()['mask'].replace('X', '0'), 2)
            and_value = int(mask.groupdict()['mask'].replace('X', '1'), 2)
        else:
            mem = re.match(mem_re, command)
            memory[mem.groupdict()['address']] = (int(mem.groupdict()['value']) | or_value) & and_value

    return sum(memory.values())


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
