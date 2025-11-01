import re

from utils.io import read_input

replacements, molecule = read_input().split("\n\n")

molecules = set()
for replacement in replacements.splitlines():
    search_molecule, replacement_molecule = replacement.split(" => ")

    for match in re.finditer(search_molecule, molecule):
        start, end = match.span()

        new_molecule = molecule[:start] + replacement_molecule + molecule[end:]
        molecules.add(new_molecule)

print(len(molecules))
