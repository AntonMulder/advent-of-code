from utils.io import read_input_lines

data = read_input_lines()

total = sum(
    len(string_literal)
    - len(bytes(string_literal, "utf-8").decode("unicode_escape")[1:-1])
    for string_literal in data
)

print(total)
