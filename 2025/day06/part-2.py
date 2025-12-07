import math
from functools import reduce

from utils.io import read_input_lines as read_data

data = read_data()
operations = [x for x in data.pop(-1) if x != " "]

temp_numbers = []
answer = 0
for index in range(0, len(data[0])):
    digits = [
        character for character in (x[index] for x in data) if character.isdigit()
    ]

    if digits:
        temp_numbers.append(int(reduce(lambda x, y: int(x) * 10 + int(y), digits)))
    else:
        answer += (
            sum(temp_numbers) if operations.pop(0) == "+" else math.prod(temp_numbers)
        )
        temp_numbers = []

answer += sum(temp_numbers) if operations.pop(0) == "+" else math.prod(temp_numbers)

print(answer)
