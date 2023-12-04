from aocd import get_data

raw = get_data(day=11, year=2021)
data = [n for n in raw.splitlines()]


def adjacent(matrix, _x, _y):
    has_left = _x > 0
    has_right = _x + 1 < len(matrix)
    has_top = _y > 0
    has_bottom = _y + 1 < len(matrix[0])

    adj = {}
    if has_left:
        adj[(_x - 1, _y)] = int(matrix[_x - 1][_y])
    if has_right:
        adj[(_x + 1, _y)] = int(matrix[_x + 1][_y])
    if has_top:
        adj[(_x, _y - 1)] = int(matrix[_x][_y - 1])
    if has_bottom:
        adj[(_x, _y + 1)] = int(matrix[_x][_y + 1])
    if has_top and has_left:
        adj[(_x - 1, _y - 1)] = int(matrix[_x - 1][_y - 1])
    if has_top and has_right:
        adj[(_x + 1, _y - 1)] = int(matrix[_x + 1][_y - 1])
    if has_bottom and has_left:
        adj[(_x - 1, _y + 1)] = int(matrix[_x - 1][_y + 1])
    if has_bottom and has_right:
        adj[(_x + 1, _y + 1)] = int(matrix[_x + 1][_y + 1])
    return adj


def forward(_x, _y, flashed, matrix):
    if (_x, _y) not in flashed:
        matrix[_x][_y] += 1
    if matrix[_x][_y] > 9:
        matrix[_x][_y] = 0
        flashed.append((_x, _y))
        adj = adjacent(matrix, _x, _y)
        [forward(*x_y, flashed, matrix) for x_y in [(a_x, a_y) for a_x, a_y in adj if (a_x, a_y) not in flashed]]


def part1(lines):
    matrix = [[int(i) for i in line] for line in lines]
    flashes, len_x, len_y = 0, len(matrix), len(matrix[0])
    for step in range(100):
        flashed = []
        for x in range(len_x):
            for y in range(len_y):
                forward(x, y, flashed, matrix)
        flashes += len(flashed)
    return flashes


print(f'Answer 1: {part1(data)}')


def part2(lines):
    matrix = [[int(i) for i in line] for line in lines]
    step, len_x, len_y = 0, len(matrix), len(matrix[0])
    while sum(sum(i) for i in matrix):
        flashed = []
        for x in range(len_x):
            for y in range(len_y):
                forward(x, y, flashed, matrix)
        step += 1
    return step


print(f'Answer 2: {part2(data)}')
