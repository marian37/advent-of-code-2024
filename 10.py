def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def find(input, r, c):
    score = set()
    distinct = 0
    stack = []
    stack.append((r, c))
    while len(stack):
        (rc, cc) = stack.pop()
        value = int(input[rc][cc])
        if value == 9:
            score.add((rc, cc))
            distinct += 1
        else:
            for rd, cd in directions:
                rn = rc + rd
                cn = cc + cd
                if rn >= 0 and rn < len(input) and cn >= 0 and cn < len(input[rn]):
                    new_value = int(input[rn][cn])
                    if new_value == value + 1:
                        stack.append((rn, cn))
    return len(score), distinct


def solve(input):
    part1 = 0
    part2 = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "0":
                score, distinct = find(input, r, c)
                part1 += score
                part2 += distinct
    return part1, part2


testInput = readInput("10_test.txt")
part1, part2 = solve(testInput)
assert part1 == 36
assert part2 == 81

input = readInput("10.txt")
part1, part2 = solve(input)
print(part1)
print(part2)
