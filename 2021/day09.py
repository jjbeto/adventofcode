from functools import reduce

from aocd import get_data

raw = get_data(day=9, year=2021)
data = [n for n in raw.splitlines()]


def adjacent(matrix, x, y):
    adj = {}
    if x > 0:
        adj[(x - 1, y)] = int(matrix[x - 1][y])
    if x + 1 < len(matrix):
        adj[(x + 1, y)] = int(matrix[x + 1][y])
    if y > 0:
        adj[(x, y - 1)] = int(matrix[x][y - 1])
    if y + 1 < len(matrix[0]):
        adj[(x, y + 1)] = int(matrix[x][y + 1])
    return adj


def part1(lines):
    lows = {}
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            pos = int(lines[x][y])
            adj = adjacent(lines, x, y)
            if pos < min(adj.values()):
                lows[(x, y)] = int(pos)
    return sum(lows.values()) + len(lows), lows


p1, lows_d = part1(data)
print(f'Answer 1: {p1}')


def part2(lines, lows):
    def basin(matrix, x, y, target=None):
        if target is None:
            target = {(x, y): int(matrix[x][y])}
        adj = {k: v for k, v in adjacent(matrix, x, y).items() if v != 9 and k not in target.keys()}
        if adj:
            target.update(adj)
            [basin(matrix, _x, _y, target) for _x, _y in adj.keys()]
        return target

    basins = [basin(lines, x, y) for x, y in lows.keys()]
    return reduce(lambda a, b: a * b, [len(b) for b in sorted(basins, key=len)[-3:]])


p2 = part2(data, lows_d)
print(f'Answer 2: {p2}')
