#!/usr/bin/env python3

with open("input.txt") as file:
    input = file.read()


SAMPLE = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

SAMPLE2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""


def parse(line):
    first = line.split("contain")
    color = first[0][:-6]

    contains = {}
    for bag in [x.strip() for x in first[1].split(",")]:
        words = bag.split(" ")
        if words[0] == "no":
            continue
        num = words[0]
        bag_color = " ".join(words[1:-1])
        contains[bag_color] = num
    return {color: contains}


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def can_contain(bag_rules, color):
    can = set()
    for parent in bag_rules.keys():
        if color in bag_rules[parent]:
            can.add(parent)
            can = can.union(can_contain(bag_rules, parent))
    return can


def must_contain(bag_rules, color):
    bags = 0
    for child, num in bag_rules.get(color, []).items():
        bags += int(num)
        bags += must_contain(bag_rules, child) * int(num)
    return bags


def solve1(input):
    bag_rules = {}
    rules = input_split(input, parse)
    for r in rules:
        bag_rules.update(r)
    return len(can_contain(bag_rules, "shiny gold"))


def solve2(input):
    bag_rules = {}
    rules = input_split(input, parse)
    for r in rules:
        bag_rules.update(r)
    return must_contain(bag_rules, "shiny gold")


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 4
    assert solve2(SAMPLE) == 32
    assert solve2(SAMPLE2) == 126

    # Part 1
    part1 = solve1(input)
    assert part1 == 254
    # print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 6006
    print(part2)
