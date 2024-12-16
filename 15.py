def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    warehouse = []
    movements = []
    for i in range(len(lines)):
        if len(lines[i]) == 0:
            warehouse = lines[:i]
            movements = lines[i + 1 :]
    return warehouse, movements


directions = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}


def move(warehouse, start, dir, part2=False):
    if part2 and dir[1] == 0:
        cr = start[0]
        cc = [[start[1]]]
        while True:
            if all([warehouse[cr][c] == "." for c in cc[-1]]):
                break
            if any([warehouse[cr][c] == "#" for c in cc[-1]]):
                return warehouse, start
            new_cc = set()
            for c in cc[-1]:
                if warehouse[cr][c] == "@":
                    new_cc.add(c)
                elif warehouse[cr][c] == "[":
                    new_cc.add(c)
                    new_cc.add(c + 1)
                elif warehouse[cr][c] == "]":
                    new_cc.add(c)
                    new_cc.add(c - 1)
            cr = cr + dir[0]
            cc.append(list(new_cc))
        while cr != start[0]:
            nr = cr - dir[0]
            nc = cc.pop()
            for c in nc:
                warehouse[cr] = (
                    warehouse[cr][:c] + warehouse[nr][c] + warehouse[cr][c + 1 :]
                )
                warehouse[nr] = warehouse[nr][:c] + "." + warehouse[nr][c + 1 :]
            cr = nr
        warehouse[cr] = warehouse[cr][: start[1]] + "." + warehouse[cr][start[1] + 1 :]
        return warehouse, (start[0] + dir[0], start[1] + dir[1])

    cr, cc = start
    while warehouse[cr][cc] != ".":
        if warehouse[cr][cc] == "#":
            return warehouse, start
        cr = cr + dir[0]
        cc = cc + dir[1]
    while (cr, cc) != start:
        nr = cr - dir[0]
        nc = cc - dir[1]
        warehouse[cr] = warehouse[cr][:cc] + warehouse[nr][nc] + warehouse[cr][cc + 1 :]
        (cr, cc) = (nr, nc)
    warehouse[cr] = warehouse[cr][:cc] + "." + warehouse[cr][cc + 1 :]
    return warehouse, (start[0] + dir[0], start[1] + dir[1])


def count(warehouse):
    result = 0
    for r in range(len(warehouse)):
        for c in range(len(warehouse[r])):
            if warehouse[r][c] == "O" or warehouse[r][c] == "[":
                result += 100 * r + c
    return result


def solve(input, part2=False):
    warehouse, movements = input
    new_warehouse = []
    for line in warehouse:
        new_warehouse.append(line)
    start = None
    for r in range(len(new_warehouse)):
        for c in range(len(new_warehouse[r])):
            if new_warehouse[r][c] == "@":
                start = (r, c)
    for line in movements:
        for l in line:
            dir = directions[l]
            new_warehouse, start = move(new_warehouse, start, dir, part2)
    return new_warehouse


def double(warehouse):
    mapping = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    new_warehouse = []
    for line in warehouse:
        new_line = ""
        for c in line:
            new_line = new_line + mapping[c]
        new_warehouse.append(new_line)
    return new_warehouse


def part1(input):
    return count(solve(input))


def part2(input):
    warehouse, movements = input
    new_warehouse = double(warehouse)
    return count(solve((new_warehouse, movements), True))


testInput = readInput("15_test.txt")
assert part1(testInput) == 2028

testInput = readInput("15_test2.txt")
assert part1(testInput) == 10092
assert part2(testInput) == 9021

input = readInput("15.txt")
print(part1(input))
print(part2(input))
