def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def solve(input):
    result1 = 0
    result2 = 0
    patterns = list(map(lambda word: word.strip(), input[0].split(",")))
    designs = input[2:]
    for design in designs:
        possible = [0 for i in range(len(design) + 1)]
        possible[0] = 1
        for i in range(1, len(design) + 1):
            for pattern in patterns:
                pl = len(pattern)
                rl = i - pl
                # print(i, pattern, pl, rl, design[rl : rl + pl], possible[rl])
                if (
                    rl >= 0
                    and (rl == 0 or possible[rl])
                    and design[rl : rl + pl] == pattern
                ):
                    possible[i] += possible[rl]
        if possible[len(design)]:
            result1 += 1
            result2 += possible[len(design)]
    return result1, result2


testInput = readInput("19_test.txt")
part1, part2 = solve(testInput)
assert part1 == 6
assert part2 == 16

input = readInput("19.txt")
part1, part2 = solve(input)
print(part1)
print(part2)
