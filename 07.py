def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def is_valid_recursive(expected, numbers, part2=False):
    if len(numbers) == 2:
        if (
            numbers[0] + numbers[1] == expected
            or numbers[0] * numbers[1] == expected
            or (part2 and int(str(numbers[0]) + str(numbers[1])) == expected)
        ):
            return True
        else:
            return False
    return (
        is_valid_recursive(expected, [numbers[0] + numbers[1]] + numbers[2:], part2)
        or is_valid_recursive(expected, [numbers[0] * numbers[1]] + numbers[2:], part2)
        or (
            part2
            and is_valid_recursive(
                expected, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:], part2
            )
        )
    )


def is_valid(expected, numbers, part2=False):
    possible = set()
    possible.add(numbers[0])
    for n in numbers[1:]:
        new_possible = set()
        for p in possible:
            new_possible.add(p + n)
            new_possible.add(p * n)
            if part2:
                new_possible.add(int(str(p) + str(n)))
        possible = new_possible
    return expected in possible


def solve(input, recursive=False):
    result = 0
    result2 = 0
    for line in input:
        left, right = line.split(":")
        expected = int(left)
        numbers = list(map(lambda n: int(n), right.strip().split(" ")))
        is_valid_function = is_valid if not recursive else is_valid_recursive
        if is_valid_function(expected, numbers):
            result += expected
            result2 += expected
        elif is_valid_function(expected, numbers, True):
            result2 += expected
    return result, result2


testInput = readInput("07_test.txt")
part1, part2 = solve(testInput)
assert part1 == 3749
assert part2 == 11387
part1, part2 = solve(testInput, True)
assert part1 == 3749
assert part2 == 11387

input = readInput("07.txt")
part1, part2 = solve(input)
print(part1)
print(part2)
part1, part2 = solve(input, True)
print(part1)
print(part2)
