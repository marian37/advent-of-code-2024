def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def parse_line(line, prize=False):
    _, desc = line.split(":")
    xdesc, ydesc = desc.split(",")
    delimiter = "=" if prize else "+"
    _, x = xdesc.split(delimiter)
    _, y = ydesc.split(delimiter)
    return int(x), int(y)


def tokens(lines, part2):
    ax, ay = parse_line(lines[0])
    bx, by = parse_line(lines[1])
    px, py = parse_line(lines[2], True)
    if part2:
        px += 10000000000000
        py += 10000000000000
    B = (py * ax - ay * px) / (ax * by - ay * bx)
    A = (px - (bx * B)) / ax
    if A.is_integer() and B.is_integer():
        return 3 * int(A) + int(B)
    else:
        return 0


def solve(input, part2=False):
    result = 0
    i = 0
    while i < len(input):
        result += tokens(input[i : i + 3], part2)
        i += 4
    return result


testInput = readInput("13_test.txt")
assert solve(testInput) == 480
print(solve(testInput, True))

input = readInput("13.txt")
print(solve(input))
print(solve(input, True))
