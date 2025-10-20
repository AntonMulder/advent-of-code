from utils.io import read_input

data = read_input()

print(abs(data.count("(") - data.count(")")))
