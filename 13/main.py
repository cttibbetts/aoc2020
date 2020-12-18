#!/usr/bin/env python3
from functools import reduce

with open("input.txt") as file:
    input = file.read()

SAMPLE = """
939
7,13,x,x,59,x,31,19
""".strip()


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def double_split(input, parse_func=lambda x: x):
    groups = input.split("\n\n")
    return [parse_func(x) for x in groups]


def parse(line):
    return line.split(",")


def find_bus(ids, time):
    while True:
        for id in ids:
            if time % id == 0:
                return id, time
        time += 1


def schedule_works(ids, time):
    for id in ids:
        if id == "x":
            time += 1
            continue
        id = int(id)
        if time % id != 0:
            return False
        time += 1
    return True


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def solve1(input):
    t = input_split(input)
    ts = int(t[0])
    ids = t[1].split(",")

    ids = sorted([int(id) for id in ids if id != "x"])

    time = ts
    id, time = find_bus(ids, time)

    delta = time - ts
    return id * delta


def solve2(input):
    t = input_split(input)
    ids = t[1].split(",")

    ids = [id for id in ids]

    n = []
    a = []

    for i, val in enumerate(ids):
        if val != "x":
            n.append(int(val))
            a.append(int(val) - i)
    out = chinese_remainder(n, a)
    return out

    """
    init = max_value - max_i
    time = init
    while True:
        if schedule_works(ids, time):
            break

        time += max_value
    print(time)
    return time
    """


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 295
    assert solve2(SAMPLE) == 1068781

    # Part 1
    part1 = solve1(input)
    assert part1 == 333
    # print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 690123192779524
    print(part2)
