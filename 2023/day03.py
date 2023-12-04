from collections import defaultdict

from aocd import get_data

import utils

raw = get_data(day=3, year=2023)
lines = raw.splitlines()

graph = utils.positional_squared_graph(len(lines))
total = 0
gears = defaultdict(list)
num = ''
neighbours = set()
for x, line in enumerate(lines):
    _y = 0
    for y, col in enumerate(line):
        if y < _y:
            continue
        _y = y
        while True:
            if _y == len(line) or not line[min(_y, len(line) - 1)].isnumeric():
                for nx, ny in neighbours:
                    elem = lines[nx][ny]
                    if not elem.isnumeric() and elem != '.' and num != '':
                        if elem == '*':
                            gears[(nx, ny)].append(int(num))
                        total += int(num)
                        break
                num, neighbours = '', set()
                break
            else:
                num += line[_y]
                neighbours.update(graph[(x, _y)])
            _y += 1

total_ratio = sum([g[0] * g[1] for g in gears.values() if len(g) == 2])

print(f'Answer 1: {total}')
print(f'Answer 2: {total_ratio}')
