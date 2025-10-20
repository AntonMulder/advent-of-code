import hashlib

counter = 0
while not hashlib.md5(f"iwrupvqb{counter}".encode()).hexdigest().startswith("000000"):
    counter += 1

print(counter)
