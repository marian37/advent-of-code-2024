def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def is_valid(expected, numbers):
    if len(numbers) == 2:
        if numbers[0] + numbers[1] == expected or numbers[0] * numbers[1] == expected:
            return True
        else:
            return False
    return is_valid(expected, [numbers[0] + numbers[1]] + numbers[2:]) or is_valid(
        expected, [numbers[0] * numbers[1]] + numbers[2:]
    )


def is_valid2(expected, numbers):
    if len(numbers) == 2:
        if (
            numbers[0] + numbers[1] == expected
            or numbers[0] * numbers[1] == expected
            or int(str(numbers[0]) + str(numbers[1])) == expected
        ):
            return True
        else:
            return False
    return (
        is_valid2(expected, [numbers[0] + numbers[1]] + numbers[2:])
        or is_valid2(expected, [numbers[0] * numbers[1]] + numbers[2:])
        or is_valid2(expected, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:])
    )


def solve(input):
    result = 0
    result2 = 0
    for line in input:
        left, right = line.split(":")
        expected = int(left)
        numbers = list(map(lambda n: int(n), right.strip().split(" ")))
        if is_valid(expected, numbers):
            result += expected
            result2 += expected
        elif is_valid2(expected, numbers):
            result2 += expected
    return result, result2


def part2(input):
    return 1


testInput = readInput("07_test.txt")
part1, part2 = solve(testInput)
assert part1 == 3749
assert part2 == 11387

input = readInput("07.txt")
part1, part2 = solve(input)
print(part1)
print(part2)
