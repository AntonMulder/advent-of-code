import math
from itertools import combinations

from utils.io import read_input_lines as read_data

junction_boxes = [tuple(map(int, line.split(","))) for line in read_data()]

combinations = [
    (
        combination,
        sum((a - b) ** 2 for a, b in zip(combination[0], combination[1], strict=True)),
    )
    for combination in combinations(junction_boxes, 2)
]

sorted_combinations = [x[0] for x in sorted(combinations, key=lambda x: x[1])]

circuits = []

for box1, box2 in sorted_combinations[:1000]:
    box_one_group_id = None
    box_two_group_id = None

    for group_id, circuit in enumerate(circuits):
        if box1 in circuit:
            box_one_group_id = group_id
        if box2 in circuit:
            box_two_group_id = group_id

    if not box_one_group_id and not box_two_group_id:
        # New group.
        circuits.append({box1, box2})
    elif box_one_group_id and not box_two_group_id:
        # Add box 2 to existing group.
        circuits[box_one_group_id].add(box2)
    elif not box_one_group_id and box_two_group_id:
        # Add box 1 to existing group.
        circuits[box_two_group_id].add(box1)
    elif box_one_group_id != box_two_group_id:
        # Combine
        circuits[box_one_group_id] |= circuits[box_two_group_id]
        del circuits[box_two_group_id]

print(math.prod(sorted([len(circuit) for circuit in circuits], reverse=True)[:3]))
