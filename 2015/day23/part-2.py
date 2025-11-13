import re

from utils.io import read_input_lines

registers = {"a": 1, "b": 0}


instructions = []
for data in read_input_lines():
    command, arguments = re.match(r"^(\S+)\s+(.*)$", data).groups()
    instruction = {"command": command}
    if command in ["hlf", "tpl", "inc"]:
        instruction["register"] = arguments
    if command == "jmp":
        instruction["offset"] = int(arguments)
    if command in ["jio", "jie"]:
        register, offset = arguments.split(", ")
        instruction["register"] = register
        instruction["offset"] = int(offset)
    instructions.append(instruction)

position = 0
while position < len(instructions):
    match instruction := instructions[position]["command"]:
        case "hlf":
            register = instructions[position]["register"]
            registers[register] //= 2
        case "tpl":
            register = instructions[position]["register"]
            registers[register] *= 3
        case "inc":
            register = instructions[position]["register"]
            registers[register] += 1
        case "jmp":
            offset = instructions[position]["offset"]
            position += int(offset) - 1
        case "jie":
            register = instructions[position]["register"]
            offset = instructions[position]["offset"]
            if registers[register] % 2 == 0:
                position += int(offset) - 1
        case "jio":
            register = instructions[position]["register"]
            offset = instructions[position]["offset"]
            if registers[register] == 1:
                position += int(offset) - 1
    position += 1

print(registers["b"])
