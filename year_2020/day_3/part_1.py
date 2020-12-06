def run(puzzle_input):

    def walk_grid(right=0, down=0, trees=0):
        if down == len(puzzle_input):
            return trees
        else:
            trees += puzzle_input[down][right] == '#'
            right = (right + 3) % len(puzzle_input[0])
            return walk_grid(right, down + 1, trees)

    return walk_grid()


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
