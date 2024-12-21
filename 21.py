from functools import cache


def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


dirpad_paths = [
    [["A"], [">A"], ["v<A"], ["vA"], [">vA", "v>A"]],  # ^
    [["<A"], ["A"], ["v<<A"], ["<vA", "v<A"], ["vA"]],  # A
    [[">^A"], [">>^A"], ["A"], [">A"], [">>A"]],  # <
    [["^A"], ["^>A", ">^A"], ["<A"], ["A"], [">A"]],  # v
    [["^<A", "<^A"], ["^A"], ["<<A"], ["<A"], ["A"]],  # >
]

directions = {"^": 0, "A": 1, "<": 2, "v": 3, ">": 4}


def get_dir_idx(input):
    return directions[input]


@cache
def find_shortest_dir(dir, iteration, part2=False):
    last = "A"
    options = set()
    options.add("")
    for d in dir:
        new_options = set()
        for option in options:
            for dp in dirpad_paths[get_dir_idx(last)][get_dir_idx(d)]:
                new_options.add(option + dp)
        last = d
        options = new_options
    best = None
    for option in options:
        if iteration > 1:
            o = option.split("A")
            s = 0
            for oo in o[:-1]:
                s += find_shortest_dir(oo + "A", iteration - 1, part2)
        else:
            s = len(option)
        if not best or s < best:
            best = s
    return best


def find_shortest(start, end, part2=False):
    (sr, sc) = start
    (er, ec) = end
    v = er - sr
    h = ec - sc
    options = set()
    if v == 0:
        if h == 0:
            options.add("A")
        elif h > 0:
            options.add("<" * h + "A")
        else:
            options.add(">" * -h + "A")
    elif v > 0:
        if h == 0:
            options.add("^" * v + "A")
        elif h > 0:
            if sr != 0 or ec != 2:
                options.add("<" * h + "^" * v + "A")
            options.add("^" * v + "<" * h + "A")
        else:
            options.add(">" * -h + "^" * v + "A")
            options.add("^" * v + ">" * -h + "A")
    else:
        if h == 0:
            options.add("v" * -v + "A")
        elif h > 0:
            options.add("<" * h + "v" * -v + "A")
            options.add("v" * -v + "<" * h + "A")
        else:
            if er != 0 or sc != 2:
                options.add("v" * -v + ">" * -h + "A")
            options.add(">" * -h + "v" * -v + "A")
    best = None
    for o in options:
        depth = 25 if part2 else 2
        s = find_shortest_dir(o, depth, part2)
        if not best or s < best:
            best = s
    return best


num_positions = [
    (0, 1),
    (1, 2),
    (1, 1),
    (1, 0),
    (2, 2),
    (2, 1),
    (2, 0),
    (3, 2),
    (3, 1),
    (3, 0),
    (0, 0),
]
dist = [[find_shortest(start, end) for end in num_positions] for start in num_positions]


def get_num_idx(input):
    if input == "A":
        return 10
    else:
        return int(input)


def solve(input):
    result = 0
    result2 = 0
    for line in input:
        last = "A"
        dist_sum = 0
        dist_sum2 = 0
        for c in line:
            dist_sum += dist[get_num_idx(last)][get_num_idx(c)]
            dist_sum2 += find_shortest(
                num_positions[get_num_idx(last)], num_positions[get_num_idx(c)], True
            )
            last = c
        result += dist_sum * int(line[:-1])
        result2 += dist_sum2 * int(line[:-1])
    return result, result2


testInput = readInput("21_test.txt")
part1, part2 = solve(testInput)
assert part1 == 126384
print(part2)

input = readInput("21.txt")
part1, part2 = solve(input)
print(part1)
print(part2)
