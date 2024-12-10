def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines[0]


def part1(input):
    result = 0
    i = 0
    li = 0
    ri = len(input) - 1
    remaining_l = int(input[li])
    remaining_r = int(input[ri])
    while True:
        if li > ri:
            return result
        free = li % 2 != 0
        if free:
            value = ri // 2
        else:
            value = li // 2
        result += i * value
        i += 1
        if remaining_l == 1:
            li += 1
            if li == ri:
                remaining_l = remaining_r - 1
            else:
                if int(input[li]) == 0:
                    li += 1
                remaining_l = int(input[li])
        else:
            remaining_l -= 1
        if free:
            if remaining_r == 1:
                ri -= 2
                remaining_r = int(input[ri])
            else:
                remaining_r -= 1


class Memory:
    def __init__(self, id, start, length, free, previous):
        self.id = id
        self.start = start
        self.length = length
        self.free = free
        self.previous = previous
        self.next = None
        self.moved = False

    def __str__(self):
        free = "F" if self.free else "O"
        prev_id = self.previous.id if self.previous else -1
        next_id = self.next.id if self.next else -1
        return f"ID: {self.id}, S: {self.start}, LEN: {self.length} {free} ({prev_id}, {next_id})"


def find_first_empty(first, moving):
    current = first
    while current and current.start < moving.start:
        if current.free and current.length >= moving.length:
            return current
        else:
            current = current.next
    return None


def part2(input):
    last = None
    first = None
    j = 0
    for i, n in enumerate(input):
        number = int(n)
        if number == 0:
            continue
        previous = last
        negative = -1 if i % 2 == 1 else 1
        last = Memory(i // 2 * negative, j, number, i % 2 == 1, last)
        if previous:
            previous.next = last
        j += number
        if not first:
            first = last

    current = last
    while current:
        if current and not current.free and not current.moved:
            empty = find_first_empty(first, current)
            if empty and empty.start < current.start:
                if empty.length == current.length:
                    t_start = empty.start
                    if empty.next == current:
                        t_prev = empty.previous
                        t_next = current.next
                        current.next = empty
                        current.previous = t_prev
                        empty.next = t_next
                        empty.previous = current
                    else:
                        t_prev = empty.previous
                        t_next = empty.next
                        empty.previous = current.previous
                        empty.next = current.next
                        current.previous = t_prev
                        current.next = t_next
                    empty.next.previous = empty
                    empty.previous.next = empty
                    current.previous.next = current
                    current.next.previous = current
                    empty.start = current.start
                    current.start = t_start
                    current.moved = True
                    current = empty
                else:
                    empty_last = Memory(
                        current.id,
                        current.start,
                        current.length,
                        True,
                        current.previous,
                    )
                    empty_last.next = current.next
                    empty_last.previous.next = empty_last
                    if empty_last.next:
                        empty_last.next.previous = empty_last
                    empty_first = Memory(
                        empty.id,
                        empty.start + current.length,
                        empty.length - current.length,
                        True,
                        current,
                    )
                    empty_first.next = empty.next
                    empty_first.previous.next = empty_first
                    empty_first.next.previous = empty_first
                    current.previous = empty.previous
                    current.next = empty_first
                    current.start = empty.start
                    current.previous.next = current
                    current.next.previous = current
                    current.moved = True
                    current = empty_last
        current = current.previous

    result = 0
    current = first
    while current:
        if not current.free:
            for i in range(current.length):
                result += (current.start + i) * current.id
        current = current.next
    return result


testInput = readInput("09_test.txt")
assert part1(testInput) == 1928
assert part2(testInput) == 2858

assert part1("12345") == 60

input = readInput("09.txt")
print(part1(input))
print(part2(input))
