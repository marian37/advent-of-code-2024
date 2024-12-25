def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def part1(input):
    last = 0
    keys = []
    locks = []
    input.append("")
    for i, line in enumerate(input):
        if line == "":
            key = True
            char = "#"
            if input[last][0] == "#":
                key = False
                char = "."

            columns = []
            for c in range(len(input[last])):
                for r in range(last, i):
                    if input[r][c] == char:
                        columns.append(r - last)
                        break
            if key:
                keys.append(columns)
            else:
                locks.append(columns)
            last = i + 1

    result = 0
    for k in range(len(keys)):
        for l in range(len(locks)):
            possible = True
            for i in range(len(keys[k])):
                if keys[k][i] < locks[l][i]:
                    possible = False
                    break
            if possible:
                result += 1
    return result


testInput = readInput("25_test.txt")
assert part1(testInput) == 3

input = readInput("25.txt")
print(part1(input))
