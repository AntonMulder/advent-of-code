from utils.io import read_input_lines

answer = 0
for bank in read_input_lines():
    batteries = [int(x) for x in bank]

    joltage = 0
    required_batteries = 12
    while (required_batteries := required_batteries - 1) >= 0:
        possible_batteries = batteries[: len(batteries) - required_batteries]
        highest_battery = max(possible_batteries)
        joltage = joltage * 10 + highest_battery
        batteries = batteries[possible_batteries.index(highest_battery) + 1 :]
    answer += joltage

print(answer)
