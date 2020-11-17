import re
from itertools import permutations


def run(puzzle_input):
    input_regex = re.compile(r'(?P<attendee>\w*) would (?P<action>gain|lose) (?P<value>\d*) happiness units '
                             r'by sitting next to (?P<neighbor>\w*)')

    # Prepare data.
    attendees = {}
    for line in puzzle_input:
        m = re.match(input_regex, line).groupdict()
        if m:
            value = int(m['value']) if m['action'] == 'gain' else - int(m['value'])
            if m['attendee'] in attendees.keys():
                attendees[m['attendee']][m['neighbor']] = value
            else:
                attendees[m['attendee']] = {m['neighbor']: value}

    people = list(attendees.keys())
    nr_people = len(people)

    happiness = 0
    for combination in permutations(people):
        combination_happiness = 0
        for i in range(nr_people):
            combination_happiness += (attendees[combination[i]][combination[(i + 1) % nr_people]] +
                                      attendees[combination[(i + 1) % nr_people]][combination[i]])
        happiness = max(happiness, combination_happiness)

    return happiness


if __name__ == '__main__':
    with open('data/puzzle_input_part_2.txt', 'r') as f:
        print(run(f.read().splitlines()))
