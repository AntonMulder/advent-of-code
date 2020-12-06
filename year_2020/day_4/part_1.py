import re


def run(puzzle_input):

    passports = (re.findall(r'\w{3}(?=:)', line.replace('\n', ' ')) for line in puzzle_input)

    def validate(passport):
        valid_codes = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        return all(code in passport for code in valid_codes)

    valid_passports = filter(lambda x: validate(x), passports)

    return sum(1 for x in valid_passports)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().split('\n\n')))
