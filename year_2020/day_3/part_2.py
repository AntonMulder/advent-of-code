def run(puzzle_input):

    def walk_grid(right=0, down=0, trees=0):
        if down >= len(puzzle_input):
            return trees
        else:
            trees += puzzle_input[down][right] == '#'
            right = (right + slope_right) % len(puzzle_input[0])
            return walk_grid(right, down + slope_down, trees)

    total_trees = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope_right, slope_down in slopes:
        total_trees *= walk_grid()

    return total_trees


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read().splitlines()))
