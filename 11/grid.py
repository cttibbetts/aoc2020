DIRECTIONS = [
    (-1, -1),  # ul
    (0, -1),  # um
    (1, -1),  # ur
    (-1, 0),  # ml
    (1, 0),  # mr
    (-1, 1),  # dl
    (0, 1),  # dm
    (1, 1),  # dr
]


class Grid:
    def __init__(self, input):
        self.grid = [[char for char in row] for row in input]

    def __repr__(self):
        string = ""
        for row in self.grid:
            for char in row:
                string += char
            string += "\n"
        return string

    def iterator(self):
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                yield (x, y, char)

    def at(self, x, y):
        if y < 0 or x < 0:
            raise IndexError
        return self.grid[y][x]

    def put(self, x, y, value):
        self.grid[y][x] = value

    def get_adjacent(self, x, y):
        adj = []
        for dx, dy in DIRECTIONS:
            try:
                adj.append(self.at(x + dx, y + dy))
            except IndexError:
                continue

        return adj

    def look(self, x, y, dx, dy, condition):
        value = self.at(x + dx, y + dy)
        if condition(value):
            return value
        return self.look(x + dx, y + dy, dx, dy, condition)

    def look_adjacent(self, x, y):
        def condition(value):
            return bool(value.strip(" ."))

        adj = []
        for dx, dy in DIRECTIONS:
            try:
                adj.append(self.look(x, y, dx, dy, condition))
            except IndexError:
                continue
        return adj
