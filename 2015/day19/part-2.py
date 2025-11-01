from random import shuffle

from utils.io import read_input

replacements, molecule = read_input().split("\n\n")

reverse_replacements = []
for replacement in replacements.split("\n"):
    left, right = replacement.split(" => ")
    reverse_replacements.append((right, left))


def find_steps(molecule: str) -> int:
    while True:
        new_molecule = molecule
        steps = 0
        while True:
            if new_molecule == "e":
                return steps
            for search, replacement in reverse_replacements:
                if search in new_molecule:
                    new_molecule = new_molecule.replace(search, replacement, 1)
                    steps += 1
                    break
            else:
                shuffle(reverse_replacements)
                break


print(find_steps(molecule))
