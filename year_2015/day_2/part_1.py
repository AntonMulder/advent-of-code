def paper_needed(dimension):
    input_list = [int(x) for x in dimension.split('x')]
    l, w, h = input_list
    side_1 = l * w
    side_2 = l * h
    side_3 = h * w
    return (2 * side_1) + (2 * side_2) + (2 * side_3) + min(side_1, side_2, side_3)


def run(puzzle_input):
    return sum(paper_needed(dimension)for dimension in puzzle_input)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
