def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def part1(input):
    left = []
    right = []
    for line in input:
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    result = 0
    for i in range(len(left)):
        result += abs(left[i] - right[i])
    return result


def part2(input):
    left = []
    right = {}
    for line in input:
        l, r = line.split("   ")
        left.append(int(l))
        rn = int(r)
        if rn in right:
            right[rn] = right[rn] + 1
        else:
            right[rn] = 1
    result = 0
    for l in left:
        r = right[l] if l in right else 0
        result += l * r
    return result


testInput = readInput("01_test.txt")
assert part1(testInput) == 11
assert part2(testInput) == 31

input = readInput("01.txt")
print(part1(input))
print(part2(input))
