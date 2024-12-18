from collections import deque


def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part1(input, size, length):
    corrupted = set()
    for i in range(length):
        line = input[i]
        x, y = line.split(",")
        corrupted.add((int(x), int(y)))
    queue = deque()
    dist = {}
    queue.append((0, 0))
    dist[(0, 0)] = 0
    while len(queue):
        cr, cc = queue.popleft()
        for dr, dc in directions:
            nr = cr + dr
            nc = cc + dc
            if (
                nr >= 0
                and nr <= size
                and nc >= 0
                and nc <= size
                and (nr, nc) not in corrupted
                and (nr, nc) not in dist
            ):
                queue.append((nr, nc))
                dist[(nr, nc)] = dist[(cr, cc)] + 1
    return dist[(size, size)] if (size, size) in dist else None


def part2(input, size):
    top = 0
    bottom = len(input)
    middle = 0
    while top < bottom:
        middle = (top + bottom) // 2
        possible = part1(input, size, middle)
        if possible:
            top = middle + 1
        else:
            bottom = middle
    return input[middle] if possible else input[middle - 1]


testInput = readInput("18_test.txt")
assert part1(testInput, 6, 12) == 22
assert part2(testInput, 6) == "6,1"

input = readInput("18.txt")
print(part1(input, 70, 1024))
print(part2(input, 70))
