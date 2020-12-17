import re


def run(puzzle_input):
    puzzle_input = puzzle_input.split('\n\n')

    # create field structure
    field_re = r'(?P<field_name>[a-z ]*): (?P<min_0>\d+)-(?P<max_0>\d+) or (?P<min_1>\d+)-(?P<max_1>\d+)'
    fields = {}

    field_data = puzzle_input[0].split('\n')
    for field in field_data:
        field_m = re.match(field_re, field).groupdict()
        fields[field_m['field_name']] = {key: int(value) for key, value in field_m.items() if key != 'field_name'}
    # Your ticket
    # Do I have to do something with it?

    # Nearby ticket
    nearby_tickets = puzzle_input[2].split('\n')

    del nearby_tickets[0]

    nearby_tickets = map(lambda x: map(int, x.split(',')), nearby_tickets)

    def validate_number(x):
        return not(any(ranges['min_0'] <= x <= ranges['max_0'] or
                       ranges['min_1'] <= x <= ranges['max_1'] for ranges in fields.values()))

    invalid_numbers = map(lambda x: filter(lambda y: validate_number(y), x), nearby_tickets)

    return sum(map(lambda x: sum(x), invalid_numbers))


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read()))
