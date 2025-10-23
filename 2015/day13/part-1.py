import re
from itertools import permutations

from utils.io import read_input_lines

data = read_input_lines()

happinesses = {}
family_members = set()

for x in data:
    first, effect, score, second = re.match(
        r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).", x
    ).groups()
    family_members.add(first)
    family_members.add(second)
    happinesses[(first, second)] = int(score) if effect == "gain" else -int(score)


def happiness_score(person: str, remaining_members: tuple[str]) -> int:
    happiness = (
        happinesses[(person, remaining_members[0])]
        + happinesses[(remaining_members[0], person)]
    )
    if len(remaining_members) > 1:
        return happiness + happiness_score(remaining_members[0], remaining_members[1:])
    return happiness


score = -1
for seating_arrangement in permutations(family_members):
    seating_arrangement += (seating_arrangement[0],)
    score = max(happiness_score(seating_arrangement[0], seating_arrangement[1:]), score)

print(score)
