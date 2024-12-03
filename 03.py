import re


def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def part1(input):
    result = 0
    for line in input:
        pattern = re.compile("mul\\((?P<x>\\d{1,3}+),(?P<y>\\d{1,3}+)\\)")
        for m in pattern.finditer(line):
            x = m.groupdict()["x"]
            y = m.groupdict()["y"]
            result += int(x) * int(y)
    return result


def part2(input):
    result = 0
    enabled = True
    for line in input:
        pattern = re.compile(
            "mul\\((?P<x>\\d{1,3}+),(?P<y>\\d{1,3}+)\\)|do\\(\\)|don\\'t\\(\\)"
        )
        for m in pattern.finditer(line):
            if m.group() == "do()":
                enabled = True
            elif m.group() == "don't()":
                enabled = False
            else:
                if enabled:
                    x = m.groupdict()["x"]
                    y = m.groupdict()["y"]
                    result += int(x) * int(y)
    return result


testInput = readInput("03_test.txt")
assert part1(testInput) == 161
testInput2 = readInput("03_test2.txt")
assert part2(testInput2) == 48

input = readInput("03.txt")
print(part1(input))
print(part2(input))
