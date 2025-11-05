houses = 36000000 // 10

presents = [0] * houses
for elf in range(1, houses):
    for house in range(elf, houses, elf):
        presents[house] += elf * 10

house = next((i for i, x in enumerate(presents) if x >= 36000000), None)
print(house)
