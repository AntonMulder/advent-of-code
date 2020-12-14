import re
from itertools import combinations


def get_addresses(mask, address):
    yield address

    floats = [35 - i for i, char in enumerate(mask) if char == 'X']
    for r in range(1, len(floats) + 1):
        for address_mask in combinations(floats, r=r):
            a = address
            for x in address_mask:
                a ^= (1 << x)
            yield a


def run(puzzle_input):
    mask_re = r'mask = (?P<mask>\w+)'
    mem_re = r'mem\[(?P<address>\d+)\] = (?P<value>\d+)'

    memory = {}
    for command in puzzle_input:
        mask_m = re.match(mask_re, command)

        if mask_m:
            mask = mask_m.groupdict()['mask']
            or_value = int(mask.replace('X', '0'), 2)
        else:
            mem_m = re.match(mem_re, command)
            value = int(mem_m.groupdict()['value'])
            address = int(mem_m.groupdict()['address']) | or_value

            for x in get_addresses(mask, address):
                memory[x] = value

    return sum(memory.values())


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
