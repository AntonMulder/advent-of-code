import re

from utils.io import read_example

password = read_example()


def next_password(password: str, index=7) -> str:
    if password[index] == "z":
        return next_password(password[:index] + "a" + password[index + 1 :], index - 1)
    return password[:index] + chr(ord(password[index]) + 1) + password[index + 1 :]


while True:
    if (
        re.search(
            r"abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz", password
        )
        and not re.search(r"i|l|o", password)
        and re.search(r"(.)\1.*(.)\2", password)
    ):
        break
    password = next_password(password)

print(password)
