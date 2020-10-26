import hashlib
import sys


def run(puzzle_input):
    for i in range(0, sys.maxsize):
        hash_result = hashlib.md5(f'{puzzle_input}{i}'.encode()).hexdigest()
        if hash_result.startswith('00000'):
            return i


if __name__ == '__main__':
    print(run('iwrupvqb'))
