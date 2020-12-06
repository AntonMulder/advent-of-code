def run(puzzle_input):
    binary_codes = map(lambda x: x.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'),
                       puzzle_input)

    seats = set([int(x, 2) for x in binary_codes])

    seat_range = set([x for x in range(min(seats), max(seats))])

    return seat_range - seats


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
