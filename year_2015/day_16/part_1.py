import re


def run(puzzle_input):
    input_re = re.compile(r'Sue (?P<id>\d*): (?P<compound_0_name>\w*): (?P<compound_0_value>\d*), '
                          r'(?P<compound_1_name>\w*): (?P<compound_1_value>\d*), (?P<compound_2_name>\w*): '
                          r'(?P<compound_2_value>\d*)')

    sue = (sue for sue in puzzle_input)
    matched_sue = (re.match(input_re, s) for s in sue)

    def is_sue(sue):
        wrapping = {
            'children': '3',
            'cats': '7',
            'samoyeds': '2',
            'pomeranians': '3',
            'akitas': '0',
            'vizslas': '0',
            'goldfish': '5',
            'trees': '3',
            'cars': '2',
            'perfumes': '1',
        }

        return (wrapping[sue['compound_0_name']] == sue['compound_0_value'] and
                wrapping[sue['compound_1_name']] == sue['compound_1_value'] and
                wrapping[sue['compound_2_name']] == sue['compound_2_value'])

    id = list(filter(lambda x: is_sue(x), matched_sue))[0]['id']

    return id


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
