import re


def run(puzzle_input):
    def passport_info(passport):
        info = {}
        for entry in passport.split(' '):
            key, value = entry.split(':')
            info[key] = value

        return info

    fixed_input = map(lambda x: x.replace('\n', ' ').strip(), puzzle_input)
    passports = map(lambda x: passport_info(x.replace('\n', ' ')), fixed_input)

    def validate(passport):
        valid_codes = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
        if all(code in passport.keys() for code in valid_codes):
            # Birth year - four digits; at least 1920 and at most 2002.
            if not (1920 <= int(passport['byr']) <= 2002):
                return False

            # Issue year - four digits; at least 2010 and at most 2020.
            if not (2010 <= int(passport['iyr']) <= 2020):
                return False

            # Expiration Year - four digits; at least 2020 and at most 2030.
            if not (2020 <= int(passport['eyr']) <= 2030):
                return False

            # Height - a number followed by either cm or in:
            #     If cm, the number must be at least 150 and at most 193.
            #     If in, the number must be at least 59 and at most 76.
            match = re.match(r'^(\d*)(cm|in)$', passport['hgt'])
            if match:
                height, unit = match.groups()
                if unit == 'cm' and not (150 <= int(height) <= 193):
                    return False
                elif unit == 'in' and not (59 <= int(height) <= 76):
                    return False
            else:
                return False

            # Hair color - a # followed by exactly six characters 0-9 or a-f.
            if not re.match(r'^#[0-9a-f]{6}', passport['hcl']):
                return False

            # Eye color - exactly one of: amb blu brn gry grn hzl oth.
            if not passport['ecl'] in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                return False

            # Passport ID - a nine-digit number, including leading zeroes.
            if not re.match(r'^[0-9]{9}$', passport['pid']):
                return False

            return True
        else:
            return False

    valid_passports = filter(lambda x: validate(x), passports)

    return sum(1 for x in valid_passports)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().split('\n\n')))
