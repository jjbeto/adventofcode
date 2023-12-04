from aocd import get_data

raw = get_data(day=5, year=2021)


def load_points(lines):
    """return dimension and coordinates"""
    _points = []
    max_x, max_y = 0, 0
    for i, line in enumerate(lines):
        _points.insert(i, ())
        for p in [_p for _p in line.split(' -> ')]:
            s = p.split(',')
            _x, _y = int(s[0]), int(s[1])
            max_x = _x if _x > max_x else max_x
            max_y = _y if _y > max_y else max_y
            _points[i] += (_x, _y)
    return (max_x + 1, max_y + 1), _points


def bresenham_algo(x0, y0, x1, y1):
    x_dist = abs(x1 - x0)
    y_dist = abs(y1 - y0)
    x, y = x0, y0
    x_inc = -1 if x0 > x1 else 1
    y_inc = -1 if y0 > y1 else 1
    line = []
    if x_dist > y_dist:
        while x != x1:
            line.append((x, y))
            x += x_inc
    elif x_dist < y_dist:
        while y != y1:
            line.append((x, y))
            y += y_inc
    else:
        while x != x1:
            line.append((x, y))
            x += x_inc
            y += y_inc
    line.append((x, y))
    return line


def part1(lines):
    dim, points = load_points(lines)
    matrix = [[0 for _ in range(dim[1])] for _ in range(dim[0])]
    for x0, y0, x1, y1 in points:
        if y0 == y1 or x0 == x1:
            for x, y in bresenham_algo(x0, y0, x1, y1):
                matrix[x][y] += 1
    return sum([1 for sublist in matrix for item in sublist if item > 1])


print(f'Answer 1: {part1(list([n for n in raw.splitlines()]))}')


def part2(lines):
    dim, points = load_points(lines)
    matrix = [[0 for _ in range(dim[1])] for _ in range(dim[0])]
    for x0, y0, x1, y1 in points:
        for x, y in bresenham_algo(x0, y0, x1, y1):
            matrix[x][y] += 1
    return sum([1 for sublist in matrix for item in sublist if item > 1])


print(f'Answer: {part2(list([n for n in raw.splitlines()]))}')
