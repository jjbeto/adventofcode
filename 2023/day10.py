from collections import defaultdict

from aocd import get_data

import utils

raw = get_data(day=10, year=2023)

#         n(-1,0)
# w(0,-1)  elem   e(0,1)
#         s(1,0)
allowed_pipes = {
    (-1, 0): ['S', '|', 'F', '7'],  # n(-1,0)
    (1, 0): ['S', '|', 'L', 'J'],  # s(1,0)
    (0, -1): ['S', '-', 'F', 'L'],  # w(0,-1)
    (0, 1): ['S', '-', 'J', '7'],  # e(0,1)
}
allowed_directions = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
    '.': [],
    'S': [(-1, 0), (1, 0), (0, -1), (0, 1)],
}
coords = utils.to_coord(raw)
matrix = utils.text_to_matrix(raw)

network = defaultdict(list)
start = ()
for x, line in enumerate(matrix):
    for y, elem in enumerate(line):
        if elem == '.':
            continue
        if elem == 'S':
            start = (x, y)
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if direction not in allowed_directions[elem]:
                continue
            coord = utils.sum_tuples(direction, (x, y))
            if coord not in coords:
                continue  # not valid coord
            direction_pipe = matrix[coord[0]][coord[1]]
            if direction_pipe not in allowed_pipes[direction]:
                continue  # not valid pipe
            network[(x, y)].append(coord)

boundaries, cur, prev = [start], network[start][0], start
while cur != start:
    boundaries.append(cur)
    if network[cur][0] != prev:
        prev = cur
        cur = network[cur][0]
    else:
        prev = cur
        cur = network[cur][1]

print(f'Answer 1: {len(boundaries) // 2}')

from matplotlib.path import Path

points, figure = [], Path(boundaries)
for x in range(len(matrix[0])):
    for y in range(len(matrix)):
        if (x, y) in boundaries:
            continue
        if figure.contains_point((x, y)):
            points.append((x, y))

print(f'Answer 2: {len(points)}')
