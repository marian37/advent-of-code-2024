def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def part1(input):
    antennas = {}
    antinodes = set()
    size = len(input)
    for r, line in enumerate(input):
        for c, character in enumerate(line):
            if character != ".":
                if character in antennas:
                    antennas[character].append((r, c))
                else:
                    antennas[character] = [(r, c)]
    for frequency in antennas:
        for i, (f1r, f1c) in enumerate(antennas[frequency]):
            for j, (f2r, f2c) in enumerate(antennas[frequency]):
                if i != j:
                    dr = f1r - f2r
                    dc = f1c - f2c
                    p1r = f1r + dr
                    p1c = f1c + dc
                    if p1r >= 0 and p1r < size and p1c >= 0 and p1c < size:
                        antinodes.add((p1r, p1c))
                    p2r = f2r - dr
                    p2c = f2c - dc
                    if p2r >= 0 and p2r < size and p2c >= 0 and p2c < size:
                        antinodes.add((p2r, p2c))
    return len(antinodes)


def part2(input):
    antennas = {}
    antinodes = set()
    size = len(input)
    for r, line in enumerate(input):
        for c, character in enumerate(line):
            if character != ".":
                if character in antennas:
                    antennas[character].append((r, c))
                else:
                    antennas[character] = [(r, c)]
    for frequency in antennas:
        for i, (f1r, f1c) in enumerate(antennas[frequency]):
            for j, (f2r, f2c) in enumerate(antennas[frequency]):
                if i != j:
                    antinodes.add((f1r, f1c))
                    antinodes.add((f2r, f2c))
                    dr = f1r - f2r
                    dc = f1c - f2c
                    pr = f1r
                    pc = f1c
                    while True:
                        pr = pr + dr
                        pc = pc + dc
                        if pr >= 0 and pr < size and pc >= 0 and pc < size:
                            antinodes.add((pr, pc))
                        else:
                            break
                    pr = f2r
                    pc = f2c
                    while True:
                        pr = pr - dr
                        pc = pc - dc
                        if pr >= 0 and pr < size and pc >= 0 and pc < size:
                            antinodes.add((pr, pc))
                        else:
                            break
    return len(antinodes)


testInput = readInput("08_test.txt")
assert part1(testInput) == 14
assert part2(testInput) == 34

input = readInput("08.txt")
print(part1(input))
print(part2(input))
