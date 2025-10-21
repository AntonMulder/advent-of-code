from utils.io import read_input_lines

data = read_input_lines()

instructions = {
    wire: instruction for instruction, wire in (x.split(" -> ") for x in data)
}

memory = {}


def run(wire: str) -> int:
    if wire.isdigit():
        return int(wire)

    if wire in memory:
        return memory[wire]

    instruction = instructions[wire]

    if instruction.isdigit():
        value = int(instruction)
    elif instruction.startswith("NOT"):
        value = ~run(instruction.split(" ")[1])
    else:
        if instruction.count(" ") == 0:
            return run(instruction)

        left, command, right = instruction.split(" ")

        match command:
            case "AND":
                value = run(left) & run(right)
            case "OR":
                value = run(left) | run(right)
            case "LSHIFT":
                value = run(left) << run(right)
            case "RSHIFT":
                value = run(left) >> run(right)

    memory[wire] = value
    return value


print(run("a"))
