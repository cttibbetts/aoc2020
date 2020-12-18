#!/usr/bin/env python3

input = "1,12,0,20,8,16"


def solve1(input):
    numbers = input.split(",")

    spoken = {}
    for i, num in enumerate(numbers[:-1]):
        spoken[num] = {"last": i + 1}

    i = len(numbers)
    while i < 2020:
        num = numbers[i - 1]

        said = spoken.get(num)
        if not said:
            numbers.append(str(0))
            spoken[str(num)] = {"last": i}
        else:
            prev = said["last"]
            said["prev"] = prev
            said["last"] = i
            numbers.append(str(i - prev))
        i += 1

    return int(numbers[-1])


def solve2(input):
    numbers = input.split(",")

    spoken = {}
    for i, num in enumerate(numbers[:-1]):
        spoken[num] = {"last": i + 1}

    i = len(numbers)
    while i < 30000000:
        num = numbers[i - 1]

        said = spoken.get(num)
        if not said:
            numbers.append(str(0))
            spoken[str(num)] = {"last": i}
        else:
            prev = said["last"]
            said["prev"] = prev
            said["last"] = i
            numbers.append(str(i - prev))
        i += 1

    return int(numbers[-1])


if __name__ == "__main__":
    # Tests
    assert solve1("1,3,2") == 1
    assert solve2("1,3,2") == 2578

    # Part 1
    part1 = solve1(input)
    assert part1 == 273
    # print(part1)

    # Part 2
    part2 = solve2(input)
    # assert part2 ==
    print(part2)
