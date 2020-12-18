#!/usr/bin/env python3

with open("input.txt") as file:
    input = file.read()


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


OP = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
}


def find_close(line, start):
    opens = 0
    idx = start
    while idx < len(line):
        char = line[idx]
        if char == "(":
            opens += 1
        if char == ")":
            opens -= 1

        if opens == 0:
            return idx
        idx += 1


def find_end_of_num(line, i, d=1):
    i += d * 2
    open = 0
    while 0 <= i and i < len(line):
        char = line[i]
        if char != " ":
            if char == "(":
                open += 1
            if char == ")":
                open -= 1

            if open == 0:
                return i
        i += d


def reformat(line):
    i = 0

    while i < len(line):
        char = line[i]
        if char == "+":
            start = find_end_of_num(line, i, -1)
            end = find_end_of_num(line, i, 1)

            line = line[:start] + "(" + line[start : end + 1] + ")" + line[end + 1 :]
            i += 1
        i += 1

    return line


def solve_equation(line):
    num_next = True
    num = 0
    operator = "+"

    idx = 0
    while idx < len(line):
        char = line[idx]
        if char == " ":
            pass
        elif num_next:
            if char == "(":
                end = find_close(line, idx)
                num = OP[operator](num, solve_equation(line[idx + 1 : end]))
                idx = end
            else:
                num = OP[operator](num, int(char))
            num_next = False
        elif char in OP:
            operator = char
            num_next = True
        idx += 1

    return num


def solve1(input):
    solves = 0
    for line in input_split(input):
        solves += solve_equation(line)
    return solves


def solve2(input):
    solves = 0
    for line in input_split(input):
        solves += solve_equation(reformat(line))
    return solves


if __name__ == "__main__":

    assert reformat("1 + 2") == "(1 + 2)"
    assert find_end_of_num("1 + 2 + (3 * 7) + 4", 6) == 14
    assert find_end_of_num("1 + 2 + (3 * 7) + 4", 6, -1) == 4
    assert find_end_of_num("1 + 2 + (3 * 7) + 4", 2) == 4
    assert find_end_of_num("1 + 2 + (3 * 7) + 4", 2, -1) == 0

    # Tests
    assert solve_equation("1 + 2 * 3 + 4 * 5 + 6") == 71
    assert solve_equation("1 + (2 * 3) + (4 * (5 + 6))") == 51
    assert solve_equation(reformat("1 + 2 * 3 + 4 * 5 + 6")) == 231
    assert solve_equation(reformat("1 + (2 * 3) + (4 * (5 + 6))")) == 51
    assert solve_equation(reformat("2 * 3 + (4 * 5)")) == 46
    assert solve_equation(reformat("5 + (8 * 3 + 9 + 3 * 4 * 3)")) == 1445

    # Part 1
    part1 = solve1(input)
    assert part1 == 1890866893020
    # print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 34646237037193
    print(part2)
