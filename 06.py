def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def will_cause_loop(position, obstacle, input):
    r, c, d = position
    ro, co = obstacle
    mem = input[ro]
    input[ro] = input[ro][:co] + "#" + input[ro][co + 1 :]
    position = (r, c, (d + 1) % 4)
    visited = set()
    while True:
        if position in visited:
            input[ro] = mem
            return True
        visited.add(position)
        r, c, d = position
        next_r = r + directions[d][0]
        next_c = c + directions[d][1]
        if next_r < 0 or next_r >= len(input) or next_c < 0 or next_c >= len(input[0]):
            input[ro] = mem
            return False
        if input[next_r][next_c] == "#":
            position = (r, c, (d + 1) % 4)
        else:
            position = (next_r, next_c, d)


def solve(input):
    position = None
    for r, line in enumerate(input):
        c = line.find("^")
        if c >= 0:
            position = (r, c, 0)
            break
    visited = set()
    loops = set()
    while True:
        r, c, d = position
        visited.add((r, c))
        next_r = r + directions[d][0]
        next_c = c + directions[d][1]
        if next_r < 0 or next_r >= len(input) or next_c < 0 or next_c >= len(input[0]):
            return len(visited), len(loops)
        if (
            input[next_r][next_c] == "."
            and (next_r, next_c) not in visited
            and (next_r, next_c) not in loops
            and will_cause_loop(position, (next_r, next_c), input)
        ):
            loops.add((next_r, next_c))
        if input[next_r][next_c] == "#":
            position = (r, c, (d + 1) % 4)
        else:
            position = (next_r, next_c, d)


testInput = readInput("06_test.txt")
part1, part2 = solve(testInput)
assert part1 == 41
assert part2 == 6

testInput = readInput("06_test2.txt")
part1, part2 = solve(testInput)
assert part2 == 1

input = readInput("06.txt")
part1, part2 = solve(input)
print(part1)
print(part2)
