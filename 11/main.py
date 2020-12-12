#!/usr/bin/env python3
import copy
from grid import Grid

with open("input.txt") as file:
    input = file.read()

SAMPLE = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip()


def input_split(input, parse_func=lambda x: x):
    groups = input.strip().split("\n")
    return [parse_func(x) for x in groups]


def double_split(input, parse_func=lambda x: x):
    groups = input.split("\n\n")
    return [parse_func(x) for x in groups]


def parse(line):
    return [seat for seat in line]


EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."


def walk(grid, x, y, dx, dy, recurse=False):
    try:
        if y + dy == -1 or x + dx == -1:
            raise IndexError
        step = grid[y + dy][x + dx]
        if recurse and step is FLOOR:
            return walk(grid, x + dx, y + dy, dx, dy, recurse)
        return step
    except IndexError:
        return None


def all_adj(grid, x, y, recurse=False):
    adj = [
        spot
        for spot in [
            walk(grid, x, y, -1, -1, recurse),  # ul
            walk(grid, x, y, 0, -1, recurse),  # u
            walk(grid, x, y, 1, -1, recurse),  # ur
            walk(grid, x, y, -1, 0, recurse),  # l
            walk(grid, x, y, 1, 0, recurse),  # r
            walk(grid, x, y, -1, 1, recurse),  # dl
            walk(grid, x, y, 0, 1, recurse),  # d
            walk(grid, x, y, 1, 1, recurse),  # dr
        ]
        if spot is not None
    ]
    return adj


def adj_occ(grid, x, y, recurse=False):
    adj = all_adj(grid, x, y, recurse)

    for s in adj:
        if s is OCCUPIED:
            return True
    return False


def all_occ(grid, x, y, recurse=False):
    adj = all_adj(grid, x, y, recurse)

    count = 0
    for s in adj:
        if s is OCCUPIED:
            count += 1

    if recurse:
        return count >= 5
    return count >= 4


def count_seats(grid):
    count = 0
    for row in grid:
        for col in row:
            if col == OCCUPIED:
                count += 1
    return count


def print_grid(grid):
    print("")
    for line in grid:
        print("".join(line))


def solve1(input):
    grid = input_split(input, parse)

    change = True
    while change:
        change = False

        new_grid = copy.deepcopy(grid)

        for y, row in enumerate(grid):

            for x, seat in enumerate(row):
                # Rule 1
                if seat is EMPTY and not adj_occ(grid, x, y):
                    new_grid[y][x] = OCCUPIED
                    change = True
                # Rule 2
                if seat is OCCUPIED and all_occ(grid, x, y):
                    new_grid[y][x] = EMPTY
                    change = True
                # Rule 3
        grid = new_grid

    count = count_seats(grid)
    return count


def solve2(input):
    grid = input_split(input, parse)

    change = True
    while change:
        change = False

        new_grid = copy.deepcopy(grid)

        for y, row in enumerate(grid):

            for x, seat in enumerate(row):
                # Rule 1
                if seat is EMPTY and not adj_occ(grid, x, y, True):
                    new_grid[y][x] = OCCUPIED
                    change = True
                # Rule 2
                if seat is OCCUPIED and all_occ(grid, x, y, True):
                    new_grid[y][x] = EMPTY
                    change = True
                # Rule 3
        grid = new_grid

    count = count_seats(grid)
    return count


def count_seats_grid(grid):
    count = 0
    for _, _, seat in grid.iterator():
        if seat is OCCUPIED:
            count += 1
    return count


def solve1_grid(input):
    grid = Grid(input_split(input, parse))

    change = True
    while change:
        change = False
        new_grid = copy.deepcopy(grid)

        for x, y, seat in grid.iterator():
            # Seat is empty and no occupied seats
            if seat is EMPTY and grid.get_adjacent(x, y).count(OCCUPIED) == 0:
                new_grid.put(x, y, OCCUPIED)
                change = True
            # Seat is occupied and 4 or more are also occupied
            if seat is OCCUPIED and grid.get_adjacent(x, y).count(OCCUPIED) >= 4:
                new_grid.put(x, y, EMPTY)
                change = True
        grid = new_grid

    count = count_seats_grid(grid)
    return count


def solve2_grid(input):
    grid = Grid(input_split(input, parse))

    change = True
    while change:
        change = False
        new_grid = copy.deepcopy(grid)

        for x, y, seat in grid.iterator():
            # Rule 1
            if seat is EMPTY and grid.look_adjacent(x, y).count(OCCUPIED) == 0:
                new_grid.put(x, y, OCCUPIED)
                change = True
            # Rule 2
            if seat is OCCUPIED and grid.look_adjacent(x, y).count(OCCUPIED) >= 5:
                new_grid.put(x, y, EMPTY)
                change = True
        grid = new_grid

    count = count_seats_grid(grid)
    return count


if __name__ == "__main__":
    # Tests

    assert solve1(SAMPLE) == 37
    assert solve2(SAMPLE) == 26

    # Part 1
    part1 = solve1(input)
    assert part1 == 2412
    # print(part1)

    # Part 2
    part2 = solve2(input)
    assert part2 == 2176
    print(part2)

    assert solve1_grid(SAMPLE) == 37
    assert solve1_grid(input) == 2412
    assert solve2_grid(SAMPLE) == 26
    assert solve2_grid(input) == 2176
