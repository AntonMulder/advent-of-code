from itertools import chain, combinations


def run(containers, eggnog):
    combination = (c for c in chain(*map(lambda x: combinations(containers, x), range(1, len(containers) + 1))))

    matches = filter(lambda x: sum(x) == eggnog, combination)

    return len(list(matches))


if __name__ == '__main__':
    print(run([43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38], 150))
