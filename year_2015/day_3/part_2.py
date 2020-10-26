def run(puzzle_input):
    visited_houses = set(['0_0'])

    for puzzle_input in (puzzle_input[0::2], puzzle_input[1::2]):
        x = y = 0
        for step in puzzle_input:
            if step == '^':
                x += 1
            elif step == 'v':
                x -= 1
            elif step == '>':
                y += 1
            elif step == '<':
                y -= 1

            house = f'{x}_{y}'
            if house not in visited_houses:
                visited_houses.add(house)

    return len(visited_houses)


if __name__ == '__main__':
    with open('data/puzzle_input.txt', 'r') as f:
        print(run(f.read()))
