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
connected_boxes = set()

while not (len(connected_boxes) == len(junction_boxes)):
    box1, box2 = sorted_combinations.pop(0)

    box_one_group_id = -1
    box_two_group_id = -1

    for idx, s in enumerate(circuits):
        if box1 in s:
            box_one_group_id = idx
        if box2 in s:
            box_two_group_id = idx

    box_one_matched = box_one_group_id > -1
    box_two_matched = box_two_group_id > -1

    if not box_one_matched and not box_two_matched:
        # New group.
        circuits.append({box1, box2})
    elif box_one_matched and not box_two_matched:
        # Add box 2 to existing group.
        circuits[box_one_group_id].add(box2)
    elif not box_one_matched and box_two_matched:
        # Add box 1 to existing group.
        circuits[box_two_group_id].add(box1)
    elif box_one_group_id != box_two_group_id:
        # Combine
        circuits[box_one_group_id] |= circuits[box_two_group_id]
        del circuits[box_two_group_id]

    connected_boxes.update({box1, box2})

else:
    print(box1[0] * box2[0])
