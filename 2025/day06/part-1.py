import math
import re

from utils.io import read_input_lines as read_data

processed_data = [re.findall(r"([\d+*]+)", x) for x in read_data()]

operations = processed_data.pop(-1)

answer = 0
for x in range(len(processed_data[0])):
    numbers = (int(y[x]) for y in processed_data)
    answer += sum(numbers) if operations[x] == "+" else math.prod(numbers)

print(answer)
