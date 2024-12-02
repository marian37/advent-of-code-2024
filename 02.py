def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def is_safe(numbers):
    decreasing = -1 if numbers[0] > numbers[1] else 1
    for i in range(len(numbers) - 1):
        d = (numbers[i + 1] - numbers[i]) * decreasing
        if d < 1 or d > 3:
            return False
    return True


def is_safe_with_remove(numbers):
    decreasing = -1 if numbers[0] > numbers[1] else 1
    for i in range(1, len(numbers)):
        d = (numbers[i] - numbers[i - 1]) * decreasing
        if d < 1 or d > 3:
            return (
                is_safe(numbers[: i - 1] + numbers[i:])
                or is_safe(numbers[:i] + numbers[i + 1 :])
                or is_safe(numbers[1:])
            )
    return True


def solve(input, allow_remove=False):
    safe = 0
    for line in input:
        is_safe_fn = is_safe_with_remove if allow_remove else is_safe
        if is_safe_fn(list(map(lambda n: int(n), line.split(" ")))):
            safe += 1
    return safe


testInput = readInput("02_test.txt")
assert solve(testInput) == 2
assert solve(testInput, True) == 4

input = readInput("02.txt")
print(solve(input))
print(solve(input, True))
