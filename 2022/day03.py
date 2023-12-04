from aocd import get_data

import utils

raw = get_data(day=3, year=2022)

total = 0
for line in raw.splitlines():
    part1, part2 = line[:len(line) // 2], line[(len(line) // 2):]
    char = ord((set(part1) & set(part2)).pop())
    # char ref: a->97 z->122 A->65 Z->90
    if char > 96:
        total += char - 96  # a=97 -> a=1
    else:
        total += char - 38  # A=65 -> A=27

print(f'Answer 1: {total}')

total = 0
for group in utils.list_by_group(raw.splitlines(), 3):
    # char ref: a->97 z->122 A->65 Z->90
    char = ord((set(group[0]) & set(group[1]) & set(group[2])).pop())
    if char > 96:
        total += char - 96  # a=97 -> a=1
    else:
        total += char - 38  # A=65 -> A=27

print(f'Answer 2: {total}')
