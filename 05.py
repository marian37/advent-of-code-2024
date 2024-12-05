def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def is_correct(numbers, rules):
    visited = set()
    for n in numbers:
        previous = rules[n] if n in rules else []
        previous = list(filter(lambda p: p in numbers, previous))
        for p in previous:
            if p not in visited:
                return False
        visited.add(n)
    return True


def sort(numbers, rules):
    for i in range(len(numbers) - 1):
        for j in range(i, len(numbers)):
            if numbers[i] in rules and numbers[j] in rules[numbers[i]]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    return numbers


def solve(input):
    update = False
    result1 = 0
    result2 = 0
    rules = {}
    for line in input:
        if line == "":
            update = True
        elif update:
            numbers = list(map(lambda n: int(n), line.split(",")))
            c = is_correct(numbers, rules)
            if c:
                result1 += numbers[len(numbers) // 2]
            else:
                sorted_numbers = sort(numbers, rules)
                result2 += sorted_numbers[len(sorted_numbers) // 2]
        else:
            xs, ys = line.split("|")
            x = int(xs)
            y = int(ys)
            if y in rules:
                rules[y].append(x)
            else:
                rules[y] = [x]
    return result1, result2


testInput = readInput("05_test.txt")
part1, part2 = solve(testInput)
assert part1 == 143
assert part2 == 123

input = readInput("05.txt")
part1, part2 = solve(input)
print(part1)
print(part2)
