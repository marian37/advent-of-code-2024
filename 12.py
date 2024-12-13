from collections import deque


def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def fill(input, visited, r, c, count):
    area = 0
    perimeter = 0
    sides = 0
    queue = deque()
    queue.append((r, c))
    character = input[r][c]
    while len(queue):
        nr, nc = queue.popleft()
        if visited[nr][nc] == -1:
            visited[nr][nc] = count
            area += 1
            for dr, dc in directions:
                rr = nr + dr
                cc = nc + dc
                if rr >= 0 and rr < len(input) and cc >= 0 and cc < len(input[rr]):
                    if input[rr][cc] == character:
                        queue.append((rr, cc))
                    else:
                        perimeter += 1
                else:
                    perimeter += 1
    for row in range(len(input)):
        current_row_up = []
        current_row_down = []
        for col in range(len(input[row])):
            if visited[row][col] == count:
                ru = row - 1
                if ru < 0 or visited[ru][col] != count:
                    current_row_up.append(col)
                rd = row + 1
                if rd >= len(input) or visited[rd][col] != count:
                    current_row_down.append(col)
        for i in range(1, len(current_row_up)):
            if current_row_up[i] != current_row_up[i - 1] + 1:
                sides += 1
        if len(current_row_up):
            sides += 1
        for i in range(1, len(current_row_down)):
            if current_row_down[i] != current_row_down[i - 1] + 1:
                sides += 1
        if len(current_row_down):
            sides += 1
    for col in range(len(input[0])):
        current_col_left = []
        current_col_right = []
        for row in range(len(input)):
            if visited[row][col] == count:
                cl = col - 1
                if cl < 0 or visited[row][cl] != count:
                    current_col_left.append(row)
                cr = col + 1
                if cr >= len(input[0]) or visited[row][cr] != count:
                    current_col_right.append(row)
        for i in range(1, len(current_col_left)):
            if current_col_left[i] != current_col_left[i - 1] + 1:
                sides += 1
        if len(current_col_left):
            sides += 1
        for i in range(1, len(current_col_right)):
            if current_col_right[i] != current_col_right[i - 1] + 1:
                sides += 1
        if len(current_col_right):
            sides += 1
    return area, perimeter, sides


def solve(input):
    result1 = 0
    result2 = 0
    visited = [[-1 for c in range(len(input[r]))] for r in range(len(input))]
    count = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if visited[r][c] == -1:
                area, perimeter, sides = fill(input, visited, r, c, count)
                count += 1
                result1 += area * perimeter
                result2 += area * sides
    return result1, result2


testInput = readInput("12_test.txt")
part1, part2 = solve(testInput)
assert part1 == 140
assert part2 == 80

testInput = readInput("12_test2.txt")
part1, part2 = solve(testInput)
assert part1 == 1930
assert part2 == 1206

testInput = readInput("12_test3.txt")
part1, part2 = solve(testInput)
assert part1 == 772
assert part2 == 436

input = readInput("12.txt")
part1, part2 = solve(input)
print(part1)
print(part2)
