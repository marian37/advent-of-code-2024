from enum import Enum
from collections import deque
import heapq


def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


class Direction(Enum):
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)
    NORTH = (-1, 0)


directions = [Direction.EAST, Direction.SOUTH, Direction.WEST, Direction.NORTH]


def find(value, end, result):
    queue = deque()
    visited = set()
    for d in range(len(directions)):
        er, ec = end
        visited.add(end)
        if value[(er, ec, d)] == result:
            queue.append((er, ec, d))
    while queue:
        current = queue.popleft()
        r, c, d = current
        visited.add((r, c))
        prev = (r - directions[d].value[0], c - directions[d].value[1], d)
        left = (r, c, (d + 1) % 4)
        right = (r, c, (d - 1) % 4)
        if prev in value and value[prev] == value[current] - 1:
            queue.append(prev)
        if left in value and value[left] == value[current] - 1000:
            queue.append(left)
        if right in value and value[right] == value[current] - 1000:
            queue.append(right)
    return len(visited)


def solve(input):
    value = {}
    nodes = []
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "S":
                for d in range(len(directions)):
                    value[(r, c, d)] = 2 << 31
                    heapq.heappush(nodes, (2 << 31, r, c, d))
                start = (r, c, 0)
                value[start] = 0
                heapq.heappush(nodes, (0, r, c, 0))
            elif input[r][c] == "E":
                end = (r, c)
                for d in range(len(directions)):
                    value[(r, c, d)] = 2 << 31
                    heapq.heappush(nodes, (2 << 31, r, c, d))
            elif input[r][c] == ".":
                for d in range(len(directions)):
                    value[(r, c, d)] = 2 << 31
                    heapq.heappush(nodes, (2 << 31, r, c, d))
    result = 2 << 31
    while nodes:
        min_value, mr, mc, md = heapq.heappop(nodes)
        min_node = (mr, mc, md)
        if min_node[0] == end[0] and min_node[1] == end[1] and min_value < result:
            result = min_value
        min_node_left = (mr, mc, (md - 1) % len(directions))
        min_node_right = (mr, mc, (md + 1) % len(directions))
        min_node_straight = (
            mr + directions[md].value[0],
            mc + directions[md].value[1],
            md,
        )
        if min_node_left in value and min_value + 1000 < value[min_node_left]:
            value[min_node_left] = min_value + 1000
            heapq.heappush(
                nodes,
                (
                    min_value + 1000,
                    min_node_left[0],
                    min_node_left[1],
                    min_node_left[2],
                ),
            )
        if min_node_right in value and min_value + 1000 < value[min_node_right]:
            value[min_node_right] = min_value + 1000
            heapq.heappush(
                nodes,
                (
                    min_value + 1000,
                    min_node_right[0],
                    min_node_right[1],
                    min_node_right[2],
                ),
            )
        if min_node_straight in value and min_value + 1 < value[min_node_straight]:
            value[min_node_straight] = min_value + 1
            heapq.heappush(
                nodes,
                (
                    min_value + 1,
                    min_node_straight[0],
                    min_node_straight[1],
                    min_node_straight[2],
                ),
            )
    count = find(value, end, result)
    return result, count


testInput = readInput("16_test.txt")
part1, part2 = solve(testInput)
assert part1 == 7036
assert part2 == 45

testInput = readInput("16_test2.txt")
part1, part2 = solve(testInput)
assert part1 == 11048
assert part2 == 64

input = readInput("16.txt")
part1, part2 = solve(input)
print(part1)
print(part2)
