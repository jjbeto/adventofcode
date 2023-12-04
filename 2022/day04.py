from aocd import get_data

import utils

raw = get_data(day=4, year=2022)

total = 0
for line in raw.splitlines():
    x1, y1, x2, y2 = utils.extract_int('%-%,%-%', line)
    if (x1 <= x2 <= y1 and x1 <= y2 <= y1) or (x2 <= x1 <= y2 and x2 <= y1 <= y2):
        total += 1

print(f'Answer 1: {total}')

total = 0
for line in raw.splitlines():
    x1, y1, x2, y2 = utils.extract_int('%-%,%-%', line)
    if x1 <= x2 <= y1 or x1 <= y2 <= y1 or x2 <= x1 <= y2 or x2 <= y1 <= y2:
        total += 1

print(f'Answer 2: {total}')
