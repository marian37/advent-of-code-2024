from collections import deque


def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(input, start, length):
    queue = deque()
    queue.append(start)
    lengths = {}
    lengths[start] = 0
    possible_cheats = set()
    while len(queue):
        cr, cc = queue.popleft()
        if lengths[(cr, cc)] >= length:
            break
        for dr, dc in directions:
            nr = cr + dr
            nc = cc + dc
            if (
                nr > 0
                and nr < len(input)
                and nc > 0
                and nc < len(input[0])
                and (nr, nc) not in lengths
            ):
                lengths[(nr, nc)] = lengths[(cr, cc)] + 1
                queue.append((nr, nc))
                if input[nr][nc] != "#":
                    possible_cheats.add(((nr, nc), lengths[(nr, nc)]))
    return possible_cheats


def bfs_dist(input, start):
    queue = deque()
    queue.append(start)
    lengths = {}
    s = len(input)
    lengths[get_index(start, s)] = 0
    while len(queue):
        cr, cc = queue.popleft()
        for dr, dc in directions:
            nr = cr + dr
            nc = cc + dc
            idx = get_index((nr, nc), s)
            if idx not in lengths and input[nr][nc] != "#":
                lengths[idx] = lengths[get_index((cr, cc), s)] + 1
                queue.append((nr, nc))
    return lengths


def get_index(point, s):
    (r, c) = point
    return r * s + c


def solve(input, save, cheats):
    start = None
    end = None
    s = len(input)
    result = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "S":
                start = (r, c)
            elif input[r][c] == "E":
                end = (r, c)
    start_dist = bfs_dist(input, start)
    end_dist = bfs_dist(input, end)
    goal = start_dist[get_index(end, s)]

    for r in range(1, len(input) - 1):
        for c in range(1, len(input[r]) - 1):
            cheat_start = (r, c)
            if input[r][c] != "#":
                possible_cheats = bfs(input, cheat_start, cheats)
                for cheat_end, cheat_length in possible_cheats:
                    if (
                        start_dist[get_index(cheat_start, s)]
                        + end_dist[get_index(cheat_end, s)]
                        + cheat_length
                        <= goal - save
                    ):
                        result += 1
    return result


testInput = readInput("20_test.txt")
assert solve(testInput, 10, 2) == 10
assert solve(testInput, 50, 20) == 285

input = readInput("20.txt")
print(solve(input, 100, 2))
print(solve(input, 100, 20))
