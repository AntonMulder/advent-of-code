from itertools import combinations

weapons = [
    {"cost": 8, "damage": 4, "armor": 0},
    {"cost": 10, "damage": 5, "armor": 0},
    {"cost": 25, "damage": 6, "armor": 0},
    {"cost": 40, "damage": 7, "armor": 0},
    {"cost": 74, "damage": 8, "armor": 0},
]

armors = [
    {"cost": 13, "damage": 0, "armor": 1},
    {"cost": 31, "damage": 0, "armor": 2},
    {"cost": 53, "damage": 0, "armor": 3},
    {"cost": 75, "damage": 0, "armor": 4},
    {"cost": 102, "damage": 0, "armor": 5},
]

rings = [
    {"cost": 25, "damage": 1, "armor": 0},
    {"cost": 50, "damage": 2, "armor": 0},
    {"cost": 100, "damage": 3, "armor": 0},
    {"cost": 20, "damage": 0, "armor": 1},
    {"cost": 40, "damage": 0, "armor": 2},
    {"cost": 80, "damage": 0, "armor": 3},
]


def attack(attacker, defender):
    damage = attacker["damage"] - defender["armor"]
    defender["hitpoints"] -= damage
    return defender["hitpoints"] <= 0


minimal_cost = 99999
for weapon in combinations(weapons, 1):
    for armor in (comb for r in range(2) for comb in combinations(armors, r)):
        for ring in (comb for r in range(3) for comb in combinations(rings, r)):
            items = weapon + armor + ring

            player = {
                "hitpoints": 100,
                "damage": sum(item["damage"] for item in items),
                "armor": sum(item["armor"] for item in items),
                "cost": sum(item["cost"] for item in items),
            }

            boss = {"hitpoints": 104, "damage": 8, "armor": 1}

            player_is_attacking = True
            while not (
                attack(player, boss) if player_is_attacking else attack(boss, player)
            ):
                player_is_attacking = not player_is_attacking

            if player_is_attacking:
                minimal_cost = min(minimal_cost, player["cost"])

print(minimal_cost)
