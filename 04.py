def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def search(input, r, c, d):
    for i, l in enumerate(["X", "M", "A", "S"]):
        rn = r + d[1] * i
        cn = c + d[0] * i
        if rn >= 0 and rn < len(input) and cn >= 0 and cn < len(input[rn]):
            if input[rn][cn] != l:
                return 0
        else:
            return 0
    return 1


def part1(input):
    result = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "X":
                for d in directions:
                    s = search(input, r, c, d)
                    result += s
    return result


def search_mas(input, r, c, w):
    corners = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
    for i, (rc, cc) in enumerate(corners):
        if input[r + rc][c + cc] != w[i]:
            return 0
    return 1


def part2(input):
    result = 0
    for r in range(1, len(input) - 1):
        for c in range(1, len(input[r]) - 1):
            if input[r][c] == "A":
                for w in ["MSSM", "SSMM", "SMMS", "MMSS"]:
                    s = search_mas(input, r, c, w)
                    result += s
    return result


testInput = readInput("04_test.txt")
assert part1(testInput) == 18
assert part2(testInput) == 9

input = readInput("04.txt")
print(part1(input))
print(part2(input))
