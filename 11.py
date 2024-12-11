def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines[0]


cache = {}
cache_usage = {}


def count(number, level):
    n = int(number)
    number = str(n)
    if (number, level) in cache:
        cache_usage[(number, level)] = (
            1
            if (number, level) not in cache_usage
            else cache_usage[(number, level)] + 1
        )
        return cache[(number, level)]
    if level == 0:
        cache[(number, level)] = 1
        return 1
    length = len(number)
    if length % 2 == 0:
        left = str(int(number[: length // 2]))
        right = str(int(number[length // 2 :]))
        result = count(left, level - 1) + count(right, level - 1)
        cache[(number, level)] = result
        return result
    next = 1 if n == 0 else n * 2024
    res = count(next, level - 1)
    cache[(number, level)] = res
    return res


def solve(input, times):
    result = 0
    for n in input.split(" "):
        result += count(n, times)
    return result


testInput = readInput("11_test.txt")
assert solve(testInput, 25) == 55312

input = readInput("11.txt")
print(solve(input, 25))
print(solve(input, 75))

# sorted_cache_usage = sorted(cache_usage.items(), key=lambda x: x[1])
# print(sorted_cache_usage)
