def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def parse_input(input):
    graph = {}
    for line in input:
        a, b = line.split("-")
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def part1(input):
    graph = parse_input(input)
    sets = set()
    for a in graph:
        if a.startswith("t"):
            for b in graph[a]:
                for c in graph[a]:
                    if c in graph[b]:
                        connected = str(sorted([a, b, c]))
                        sets.add(connected)
    return len(sets)


def find_largest(graph, start, taken, i):
    if i == len(graph[start]):
        return taken
    else:
        k = []
        if all(list(map(lambda t: graph[start][i] in graph[t], taken))):
            taken.add(graph[start][i])
            k = find_largest(graph, start, taken, i + 1)
        l = find_largest(graph, start, taken, i + 1)
        return l if len(l) > len(k) else k


def part2(input):
    graph = parse_input(input)
    result = []
    for a in graph:
        if a.startswith("t"):
            largest = find_largest(graph, a, {a}, 0)
            if len(largest) > len(result):
                result = largest
    return ",".join(sorted(result))


testInput = readInput("23_test.txt")
assert part1(testInput) == 7
assert part2(testInput) == "co,de,ka,ta"

input = readInput("23.txt")
print(part1(input))
print(part2(input))
