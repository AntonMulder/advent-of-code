import hashlib

from utils.io import read_input

data = read_input()

counter = 0
while not hashlib.md5(f"{data}{counter}".encode()).hexdigest().startswith("000000"):
    counter += 1

print(counter)
