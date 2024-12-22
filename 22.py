def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def mix(secret, value):
    return secret ^ value


def prune(secret):
    return secret % 16777216


def next(secret):
    value = secret * 64
    secret = mix(secret, value)
    secret = prune(secret)
    value = secret // 32
    secret = mix(secret, value)
    secret = prune(secret)
    value = secret * 2048
    secret = mix(secret, value)
    secret = prune(secret)
    return secret


def solve(input):
    result = 0
    bananas = []
    changes = []
    for line in input:
        n = int(line)
        bananas.append([])
        changes.append([])
        for i in range(2000):
            bananas[-1].append(n % 10)
            changes[-1].append(
                None if not len(changes[-1]) else bananas[-1][-1] - bananas[-1][-2]
            )
            n = next(n)
        result += n

    sequences = {}
    for i, changes_list in enumerate(changes):
        applied = set()
        for j in range(1, len(changes_list) - 4):
            sequence = str(changes_list[j : j + 4])
            value = bananas[i][j + 3]
            if sequence not in applied:
                if sequence in sequences:
                    sequences[sequence] += value
                else:
                    sequences[sequence] = value
                applied.add(sequence)
    m = max(sequences, key=sequences.get)
    return result, sequences[m]


testInput = readInput("22_test.txt")
part1, part2 = solve(testInput)
assert part1 == 37327623
print(part2)

input = readInput("22.txt")
part1, part2 = solve(input)
print(part1)
print(part2)
