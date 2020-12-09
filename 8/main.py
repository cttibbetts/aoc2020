#!/usr/bin/env python3
from console import Console, LoopDetectedError, EndOfProgram

with open("input.txt") as file:
    input = file.read()


SAMPLE = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip()


SAMPLE2 = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip()


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def run_program(program):
    accumulator = 0
    ptr = 0
    while ptr < len(program):
        instruction = program[ptr]
        if instruction is None:
            raise Exception(accumulator)

        op, val = instruction.split(" ")
        program[ptr] = None

        if op == "acc":
            accumulator += int(val)
        elif op == "jmp":
            ptr += int(val)
            continue
        elif op == "nop":
            pass
        ptr += 1
    return accumulator


def solve1(input):
    program = input_split(input)
    try:
        return run_program(program)
    except Exception as e:
        return int(str(e))


def solve2(input):
    program = input_split(input)

    for ptr, instruction in enumerate(program):
        op, val = instruction.split(" ")
        p = [i for i in program]  # copy program
        if op == "jmp":
            p[ptr] = p[ptr].replace("jmp", "nop")
        elif op == "nop":
            p[ptr] = p[ptr].replace("nop", "jmp")
        else:
            # Not an option
            continue

        try:
            out = run_program(p)
            return out
        except Exception:
            pass


def solve1_class(input):
    program = Console(input_split(input))
    try:
        program.run()
    except LoopDetectedError as e:
        return e.value


def solve2_class(input):
    program = input_split(input)

    for ptr, instruction in enumerate(program):
        p = Console(program)
        if instruction.startswith("jmp"):
            p.edit(ptr, op="nop")
        elif instruction.startswith("nop"):
            p.edit(ptr, op="jmp")
        else:
            continue

        try:
            p.run()
        except LoopDetectedError:
            continue
        except EndOfProgram as e:
            return e.value


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 5
    assert solve2(SAMPLE2) == 8

    # Part 1
    part1 = solve1(input)
    assert part1 == 1801
    # print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 2060
    print(part2)

    assert solve1_class(SAMPLE) == 5
    assert solve1_class(input) == 1801
    assert solve2_class(SAMPLE2) == 8
    assert solve2_class(input) == 2060
