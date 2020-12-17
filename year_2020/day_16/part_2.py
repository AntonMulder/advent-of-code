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
    your_ticket = [int(x) for x in puzzle_input[1].split('\n')[1].split(',')]

    # Nearby ticket
    nearby_tickets = puzzle_input[2].split('\n')
    del nearby_tickets[0]
    nearby_tickets = map(lambda x: list(map(int, x.split(','))), nearby_tickets)

    def validate_ticket(ticket):
        return all(any(ranges['min_0'] <= x <= ranges['max_0'] or
                       ranges['min_1'] <= x <= ranges['max_1'] for ranges in fields.values())
                   for x in ticket)

    valid_tickets = list(filter(lambda x: validate_ticket(x), nearby_tickets))

    field_possibilities = {index: list(fields.keys()) for index in range(0, len(your_ticket))}

    # Do one round to remove invalid columns.
    for index in range(0, len(your_ticket)):
        for field in fields.keys():
            ranges = fields[field]
            if not(all(ranges['min_0'] <= x[index] <= ranges['max_0'] or
                   ranges['min_1'] <= x[index] <= ranges['max_1'] for x in valid_tickets)):
                field_possibilities[index].remove(field)

    # Keep removing possible field names until all have 1 field name.
    while sum(map(lambda x: len(x), field_possibilities.values())) > len(your_ticket):
        for index in range(len(your_ticket)):
            if len(field_possibilities[index]) == 1:
                field_name = field_possibilities[index][0]
                for i in field_possibilities:
                    if i != index and field_name in field_possibilities[i]:
                        field_possibilities[i].remove(field_name)

    possibilities_list = list(map(lambda x: x[0], field_possibilities.values()))
    departure_fields = filter(lambda x: 'departure' in x, possibilities_list)
    departure_indexes = map(lambda x: possibilities_list.index(x), departure_fields)

    total = 1
    for index in departure_indexes:
        total *= your_ticket[index]

    return total


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read()))
