def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def parse_line(line):
    p, v = line.split(" ")
    _, p = p.split("=")
    _, v = v.split("=")
    px, py = p.split(",")
    vx, vy = v.split(",")
    return int(px), int(py), int(vx), int(vy)


def part1(input, sx, sy):
    shx = sx // 2
    shy = sy // 2
    quadrants = [0, 0, 0, 0]
    seconds = 100
    for line in input:
        px, py, vx, vy = parse_line(line)
        npx = (px + seconds * vx) % sx
        npy = (py + seconds * vy) % sy
        if npx != shx and npy != shy:
            qx = npx < shx
            qy = npy < shy
            quadrants[2 * qy + qx] += 1
    result = 1
    for q in quadrants:
        result *= q
    return result


def print_robots(robots):
    for line in robots:
        for l in line:
            print(l, end="")
        print()
    print()


def check_robots(positions):
    for row in range(len(positions)):
        subsequent = 0
        for col in range(len(positions[row])):
            if positions[row][col] == "#":
                subsequent += 1
            else:
                subsequent = 0
            if subsequent > 10:
                return True
    return False


def part2(input, sx, sy):
    robots = list()
    for line in input:
        robot = parse_line(line)
        robots.append(robot)
    second = 0
    while True:
        positions = [[" " for x in range(sx)] for y in range(sy)]
        for robot in robots:
            px, py, vx, vy = robot
            npx = (px + second * vx) % sx
            npy = (py + second * vy) % sy
            positions[npy][npx] = "#"
        if check_robots(positions):
            print_robots(positions)
            return second
        second += 1


testInput = readInput("14_test.txt")
assert part1(testInput, 11, 7) == 12

input = readInput("14.txt")
print(part1(input, 101, 103))
print(part2(input, 101, 103))
