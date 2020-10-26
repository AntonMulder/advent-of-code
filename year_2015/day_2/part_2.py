def paper_needed(dimension):
    input_list = [int(x) for x in dimension.split('x')]
    l, w, h = input_list
    return (l * w * h) + min(l + l + w + w, l + l + h + h, w + w + h + h)


def run(puzzle_input):
    return sum(paper_needed(dimension) for dimension in puzzle_input)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
