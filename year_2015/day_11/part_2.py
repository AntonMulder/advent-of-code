import re


def next_password(password, index=7):
    if password[index] == 'z':
        return next_password(password[:index] + 'a' + password[index+1:], index-1)
    return password[:index] + chr(ord(password[index]) + 1) + password[index+1:]


def run(password):
    three_letters = re.compile(r'abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz')
    contain = re.compile(r'i|l|o')
    pairs = re.compile(r'(.)\1.*(.)\2')
    skip_once = True

    while True:
        if (re.search(three_letters, password) and
                not re.search(contain, password) and
                re.search(pairs, password)):
            if skip_once:
                skip_once = False
            else:
                break
        password = next_password(password)

    return password


if __name__ == '__main__':
    print(run('hxbxwxba'))
