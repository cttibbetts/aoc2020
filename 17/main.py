#!/usr/bin/env python3

with open("input.txt") as file:
    input = file.read()

SAMPLE = """
.#.
..#
###
""".strip()


def parse(line):
    return line


def get_neighbors(coords, known=[]):
    d = int(coords[0])

    neighbors = []
    for d in range(d - 1, d + 2):
        c = known + [str(d)]
        if len(coords) > 1:
            neighbors += get_neighbors(coords[1:], c)
        else:
            neighbors.append(c)

    return [n for n in neighbors if n != coords]


def solve1(input):
    grid = {}
    rows = input.strip().split("\n")
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            if col == "#":
                grid[f"{x},{y},0"] = True

    cycle = 1
    while cycle <= 6:
        new_grid = {}
        neighbor_touch = {}
        for key, active in grid.items():
            coords = key.split(",")
            active_neighbors = []
            for n in get_neighbors(coords):
                nc = ",".join(n)
                if grid.get(nc):
                    active_neighbors.append(nc)

                nt = neighbor_touch.get(nc, 0)
                neighbor_touch[nc] = nt + 1

            an = len(active_neighbors)
            if 2 <= an and an <= 3:
                new_grid[key] = True

        activators = [n for n, count in neighbor_touch.items() if count == 3]
        for a in activators:
            if grid.get(a) is None:
                new_grid[a] = True

        grid = new_grid
        cycle += 1

    return len(grid)


def solve2(input):
    grid = {}
    rows = input.strip().split("\n")
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            if col == "#":
                grid[f"{x},{y},0,0"] = True

    cycle = 1
    while cycle <= 6:
        new_grid = {}
        neighbor_touch = {}
        for key, active in grid.items():
            coords = key.split(",")
            active_neighbors = []
            for n in get_neighbors(coords):
                nc = ",".join(n)
                if grid.get(nc):
                    active_neighbors.append(nc)

                nt = neighbor_touch.get(nc, 0)
                neighbor_touch[nc] = nt + 1

            an = len(active_neighbors)
            if 2 <= an and an <= 3:
                new_grid[key] = True

        activators = [n for n, count in neighbor_touch.items() if count == 3]
        for a in activators:
            if grid.get(a) is None:
                new_grid[a] = True

        grid = new_grid
        cycle += 1

    return len(grid)


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 112
    assert solve2(SAMPLE) == 848

    # Part 1
    part1 = solve1(input)
    assert part1 == 401
    # print(part1)

    # Part 2
    part2 = solve2(input)
    # assert part2 ==
    print(part2)
