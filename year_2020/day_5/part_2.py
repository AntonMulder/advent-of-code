def run(puzzle_input):
    binary_codes = map(lambda x: x.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'),
                       puzzle_input)
    seat_codes = map(lambda x: int(x, 2), binary_codes)

    seats = set(seat_codes)

    missing_seat = filter(lambda x: x not in seats, range(0, max(seats)))

    seat = filter(lambda x: x - 1 in seats and x + 1 in seats, missing_seat)

    return max(seat)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
