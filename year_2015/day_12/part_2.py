import json


def find_number(data):

    if isinstance(data, list):
        return sum([find_number(i) for i in data])
    elif isinstance(data, dict):
        if 'red' in data.values():
            return 0
        return sum([find_number(i) for i in data.values()])
    elif isinstance(data, int):
        return data
    return 0


def run(puzzle_input):
    data = json.loads(puzzle_input)
    return find_number(data)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read()))
