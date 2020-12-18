#!/usr/bin/env python3

with open("input.txt") as file:
    input = file.read()

SAMPLE = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".strip()

SAMPLE2 = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".strip()


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def double_split(input, parse_func=lambda x: x):
    groups = input.split("\n\n")
    return [parse_func(x) for x in groups]


def parse(line):
    return [x.strip() for x in line.split("=")]


def solve1(input):
    code = input_split(input, parse)
    mask = ""
    memory = {}
    for line in code:
        if line[0] == "mask":
            mask = line[1]

        else:
            mem = line[0][4:-1]
            value = "{0:b}".format(int(line[1])).zfill(36)
            for i, char in enumerate(mask):
                if char != "X":
                    value = value[:i] + char + value[i + 1 :]
            memory[mem] = int(value, 2)

    sum = 0
    for _, val in memory.items():
        sum += val

    return sum


def get_options(mem, start=0):
    for i in range(start, len(mem)):
        if mem[i] == "X":
            mem0 = mem[:i] + "0" + mem[i + 1 :]
            mem1 = mem[:i] + "1" + mem[i + 1 :]
            return get_options(mem0, i + 1) + get_options(mem1, i + 1)
    return [mem]


def solve2(input):
    code = input_split(input, parse)
    mask = ""
    memory = {}
    for line in code:
        if line[0] == "mask":
            mask = line[1]

        else:
            mem = "{0:b}".format(int(line[0][4:-1])).zfill(36)
            value = int(line[1])

            for i, char in enumerate(mask):
                if char == "0":
                    continue
                elif char == "1":
                    mem = mem[:i] + "1" + mem[i + 1 :]
                elif char == "X":
                    mem = mem[:i] + "X" + mem[i + 1 :]

            for option in get_options(mem):
                memory[int(option, 2)] = value

    sum = 0
    for _, val in memory.items():
        sum += val

    return sum


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 165
    assert solve2(SAMPLE2) == 208

    # Part 1
    part1 = solve1(input)
    assert part1 == 8332632930672
    # print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 4753238784664
    print(part2)
