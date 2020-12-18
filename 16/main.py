#!/usr/bin/env python3

with open("input.txt") as file:
    input = file.read()

SAMPLE = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".strip()

SAMPLE2 = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
""".strip()


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def validate_num(rules, number):
    for rule, ranges in rules.items():
        for r in ranges:
            low = int(r[0])
            hi = int(r[1])

            if low <= number and number <= hi:
                return True
    return False


def invalid_values(rules, ticket):
    invalids = []
    for num in ticket:
        if validate_num(rules, int(num)):
            continue
        else:
            invalids.append(num)
    return invalids


def match_rule(ranges, number):
    for r in ranges:
        low = int(r[0])
        hi = int(r[1])

        if low <= number and number <= hi:
            return True
    return False


def validate_ticket(rules, ticket):
    for num in ticket:
        if validate_num(rules, int(num)):
            continue
        else:
            return False
    return True


def solve1(input):
    rules = {}
    tickets = []
    f_rules = True
    f_my = False
    f_near = False
    for line in input_split(input):
        if line == "":
            continue
        if line == "your ticket:":
            f_rules = False
            f_my = True
            continue
        if line == "nearby tickets:":
            f_my = False
            f_near = True
            continue

        if f_rules:
            a = line.split(":")
            rule = a[0]
            ranges = a[1].split(" or ")
            rules[rule] = [r.split("-") for r in ranges]
        elif f_my:
            continue
        elif f_near:
            tickets.append(line.split(","))

    invalids = []
    for ticket in tickets:
        invalids += invalid_values(rules, ticket)

    sum = 0
    for i in invalids:
        sum += int(i)
    return sum


def resolve_rules(possible, output=[None] * 20):
    removals = []
    for i, ruleset in enumerate(possible):
        if len(ruleset) == 1:
            rule = list(ruleset)[0]
            output[i] = rule
            removals.append(rule)
    if removals:
        for idx, _ in enumerate(possible):
            for r in removals:
                try:
                    possible[idx].remove(r)
                except Exception:
                    continue
        return resolve_rules(possible, output)
    return output


def solve2(input):
    rules = {}
    my_ticket = []
    tickets = []
    f_rules = True
    f_my = False
    f_near = False
    for line in input_split(input):
        if line == "":
            continue
        if line == "your ticket:":
            f_rules = False
            f_my = True
            continue
        if line == "nearby tickets:":
            f_my = False
            f_near = True
            continue

        if f_rules:
            a = line.split(":")
            rule = a[0]
            ranges = a[1].split(" or ")
            rules[rule] = [r.split("-") for r in ranges]
        elif f_my:
            my_ticket = line.split(",")
        elif f_near:
            tickets.append(line.split(","))

    valid_tickets = [ticket for ticket in tickets if validate_ticket(rules, ticket)]

    possible = [set(rules.keys()) for _ in my_ticket]

    for ticket in valid_tickets:
        for i, val in enumerate(ticket):
            num = int(val)

            removals = []
            for rule in possible[i]:
                ranges = rules[rule]
                if not match_rule(ranges, num):
                    removals.append(rule)
            for r in removals:
                possible[i].remove(r)

    resolved = resolve_rules(possible)

    mult = 1
    for i, rule in enumerate(resolved):
        if rule is not None and rule[:9] == "departure":
            mult *= int(my_ticket[i])
    return mult


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 71
    assert solve2(SAMPLE2)

    # Part 1
    part1 = solve1(input)
    assert part1 == 27802
    # print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 279139880759
    print(part2)
