#!/usr/bin/env python3
from functools import lru_cache
import itertools

with open("input.txt") as file:
    input = file.read()

SAMPLE = """
16
10
15
5
1
11
7
19
6
12
4
""".strip()

SAMPLE2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".strip()


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def double_split(input, parse_func=lambda x: x):
    groups = input.split("\n\n")
    return [parse_func(x) for x in groups]


def parse(line):
    return int(line)
    return line


def solve1(input):
    ones = 0
    threes = 0

    adapters = sorted(input_split(input, parse))
    adapters = [0] + adapters + [adapters[-1] + 3]
    prev = adapters[0]
    for ad in adapters:
        diff = ad - prev
        if diff == 1:
            ones += 1
        if diff == 3:
            threes += 1
        prev = ad

    return ones * threes


# @lru_cache
def count_chain(chain_num):
    chain = range(chain_num)
    chain = [*range(1, chain_num + 1)]

    count = 0
    for r in range(2, chain_num + 1):
        perms = itertools.combinations(chain, r=r)
        for perm in perms:
            perm = [-2] + list(perm) + [chain_num + 3]
            prev = perm[0]
            valid = True
            for ad in perm[1:]:
                diff = ad - prev
                if diff > 3:
                    valid = False
                    break
                prev = ad
            if valid:
                count += 1
    return count


def solve2(input):
    perms = 1
    adapters = sorted(input_split(input, parse))
    adapters = [0] + adapters + [adapters[-1] + 3]

    chains = []
    new_chain = [0]
    prev = 0
    for idx, ad in enumerate(adapters):
        diff = ad - prev
        if diff == 1:
            # in chain
            new_chain.append(ad)
        elif diff == 2:
            raise Exception("there was a 2")
        elif diff == 3:
            # end chain
            if len(new_chain) >= 3:
                chains.append(new_chain)
            new_chain = [ad]
        prev = ad

    perms = 1
    for chain in chains:
        length = len(chain)
        perms = perms * count_chain(length)

    return perms


if __name__ == "__main__":
    # Tests
    assert count_chain(2) == 1
    assert count_chain(3) == 2
    assert count_chain(4) == 4
    assert count_chain(5) == 7

    assert solve1(SAMPLE) == 35
    assert solve2(SAMPLE) == 8
    assert solve2(SAMPLE2) == 19208

    # Part 1
    part1 = solve1(input)
    assert part1 == 2470

    # Part 2
    part2 = solve2(input)
    assert part2 == 1973822685184
    print(part2)
