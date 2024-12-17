def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def execute(registers, i, instruction, operand):
    operand_value = (
        operand if operand < 4 or instruction in ["1", "3"] else registers[operand - 4]
    )
    output = None
    next = i + 2
    match instruction:
        case "0":
            registers[0] = registers[0] // (2**operand_value)
        case "1":
            registers[1] = registers[1] ^ operand
        case "2":
            registers[1] = operand_value % 8
        case "3":
            if registers[0] != 0:
                next = operand
        case "4":
            registers[1] = registers[1] ^ registers[2]
        case "5":
            output = str(operand_value % 8)
        case "6":
            registers[1] = registers[0] // (2**operand_value)
        case "7":
            registers[2] = registers[0] // (2**operand_value)
    return registers, output, next


def part1(input):
    registers = list(map(lambda line: int(line.split(" ")[-1]), input[:3]))
    program = input[-1].split(" ")[-1].split(",")

    result = []
    i = 0
    while i < len(program):
        registers, output, next = execute(registers, i, program[i], int(program[i + 1]))
        i = next
        if output:
            result.append(output)
    return ",".join(result)


def dfs(registers_original, program, a, iteration):
    res = None
    for b in range(0o10):
        registers = registers_original.copy()
        registers[0] = a * 8 + b
        result = []
        i = 0
        while i < len(program):
            registers, output, next = execute(
                registers, i, program[i], int(program[i + 1])
            )
            i = next
            if output:
                result.append(output)
        if result[0] == program[len(program) - 1 - iteration]:
            if len(result) == len(program):
                return a * 8 + b
            else:
                d = dfs(registers_original, program, a * 8 + b, iteration + 1)
                if d and (not res or d < res):
                    res = d
    return res


def part2(input):
    registers_original = list(map(lambda line: int(line.split(" ")[-1]), input[:3]))
    program = input[-1].split(" ")[-1].split(",")

    return dfs(registers_original, program, 0, 0)


testInput = readInput("17_test.txt")
assert part1(testInput) == "4,6,3,5,6,3,5,2,1,0"
testInput = readInput("17_test2.txt")
assert part2(testInput) == 117440

input = readInput("17.txt")
print(part1(input))
print(part2(input))
