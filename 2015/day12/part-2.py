import json

from utils.io import read_input

data = json.loads(read_input())


def sum_numbers(data) -> int:
    if isinstance(data, list):
        return sum([sum_numbers(x) for x in data])
    elif isinstance(data, dict):
        if "red" in data.values():
            return 0
        return sum([sum_numbers(i) for i in data.values()])
    elif isinstance(data, int):
        return data
    return 0


print(sum_numbers(data))
