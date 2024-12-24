from collections import deque


def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def parse_input(input):
    initial = {}
    instructions = {}

    read_instructions = False
    for line in input:
        if line == "":
            read_instructions = True
        elif read_instructions:
            instruction = line.split(" ")
            instructions[instruction[-1]] = instruction
        else:
            wire, value = line.split(": ")
            initial[wire] = int(value)

    return initial, instructions


def process_instruction(values, instruction):
    a = instruction[0]
    b = instruction[2]
    c = instruction[4]
    operation = instruction[1]
    if operation == "AND":
        res = values[a] & values[b]
    elif operation == "OR":
        res = values[a] | values[b]
    else:
        res = values[a] ^ values[b]
    return c, res


def part1(input):
    result = 0
    values, instructions = parse_input(input)
    unhandled_instructions = deque()
    for i in instructions:
        unhandled_instructions.append(i)
    while len(unhandled_instructions):
        i = unhandled_instructions.popleft()
        if instructions[i][0] in values and instructions[i][2] in values:
            output, output_value = process_instruction(values, instructions[i])
            values[output] = output_value
        else:
            unhandled_instructions.append(i)
    for z in values:
        if z.startswith("z") and values[z]:
            c = int(z[1:])
            result += 1 << c
    return result


def check(instructions, z, last):
    z_key = f"z{z:02d}"
    instr = instructions[z_key]

    z_same = [f"x{z:02d}", f"y{z:02d}"]
    z_minor = [f"x{z-1:02d}", f"y{z-1:02d}", last[0], last[1]]

    if instr[1] != "XOR":
        return [instr[0], instr[2]], instr[4]

    i_xor_key = instr[0] if instructions[instr[0]][1] == "XOR" else instr[2]
    i_xor = instructions[i_xor_key]
    if i_xor[1] != "XOR" or i_xor[0] not in z_same or i_xor[2] not in z_same:
        return [instr[0], instr[2]], i_xor[4]

    i_or_key = instr[2] if instructions[instr[2]][1] == "OR" else instr[0]
    i_or = instructions[i_or_key]
    if i_or[1] != "OR":
        return [instr[0], instr[2]], i_or[4]

    i_or_first = instructions[i_or[0]]
    if (
        i_or_first[1] != "AND"
        or i_or_first[0] not in z_minor
        or i_or_first[2] not in z_minor
    ):
        return [instr[0], instr[2]], i_or_first[4]

    i_or_second = instructions[i_or[2]]
    if (
        i_or_second[1] != "AND"
        or i_or_second[0] not in z_minor
        or i_or_second[2] not in z_minor
    ):
        return [instr[0], instr[2]], i_or_second[4]

    return [instr[0], instr[2]], None


def part2(input):
    _, instructions = parse_input(input)
    last = ["nmk", "dsr"]
    all_swapped = set()
    for z in range(2, 45):
        last, swapped = check(instructions, z, last)
        if swapped:
            all_swapped.add(swapped)
    return ",".join(sorted(all_swapped))


testInput = readInput("24_test.txt")
assert part1(testInput) == 4

testInput = readInput("24_test2.txt")
assert part1(testInput) == 2024

input = readInput("24.txt")
print(part1(input))
print(part2(input))
