def run(puzzle_input, invalid_number):
    numbers = list(map(int, puzzle_input))

    slice_size = 2
    while True:
        for index in range(slice_size, len(numbers) + 1):
            contiguous_set = numbers[index - slice_size: index]

            if sum(contiguous_set) == invalid_number:
                return min(contiguous_set) + max(contiguous_set)

        slice_size += 1


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines(), 507622668))
