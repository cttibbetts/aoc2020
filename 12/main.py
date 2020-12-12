#!/usr/bin/env python3

with open("input.txt") as file:
    input = file.read()

SAMPLE = """
F10
N3
F7
R90
F11
""".strip()


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def parse(line):
    return line


def move(x, y, amount, op):
    if op == "N":
        y += amount
    elif op == "S":
        y -= amount
    elif op == "E":
        x += amount
    elif op == "W":
        x -= amount

    return x, y


DIRECTIONS = ["N", "E", "S", "W"]


def manhattan(n1, n2):
    dist = 0
    dist += abs(n1[0] - n2[0])
    dist += abs(n1[1] - n2[1])
    return dist


def turn(facing, amount, dir):
    value = int(amount / 90)

    for _ in range(0, value):
        if dir == "L":
            facing -= 1
        elif dir == "R":
            facing += 1
        if facing == -1:
            facing = 3
        elif facing == 4:
            facing = 0
    return facing


def rotate(x, y, amount, dir):
    value = int(amount / 90)

    for _ in range(0, value):
        if dir == "L":
            buf = x
            x = -y
            y = buf
        if dir == "R":
            buf = x
            x = y
            y = -buf
    return x, y


def move_to_waypoint(x, y, dx, dy, repeat):
    for _ in range(0, repeat):
        x += dx
        y += dy
    return x, y


def solve1(input):
    x = 0
    y = 0
    facing = 1
    for line in input_split(input, parse):
        op = line[0]
        num = int(line[1:])

        if op in ("R", "L"):
            facing = turn(facing, num, op)
        elif op == "F":
            x, y = move(x, y, num, DIRECTIONS[facing])
        else:
            x, y = move(x, y, num, op)

    out = manhattan([0, 0], [x, y])
    return out


def solve2(input):
    wx = 10
    wy = 1
    x = 0
    y = 0
    for line in input_split(input, parse):
        op = line[0]
        num = int(line[1:])

        if op in ("R", "L"):
            wx, wy = rotate(wx, wy, num, op)
        elif op == "F":
            # move the ship
            x, y = move_to_waypoint(x, y, wx, wy, num)
        else:
            # move the waypoint
            wx, wy = move(wx, wy, num, op)

    out = manhattan([0, 0], [x, y])
    return out


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 25
    assert solve2(SAMPLE) == 286

    # Part 1
    part1 = solve1(input)
    assert part1 == 1186
    # print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 47806
    print(part2)
