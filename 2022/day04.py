from aocd import get_data

import utils

raw = get_data(day=4, year=2022)

answer_1 = 0
answer_2 = 0

for line in raw.splitlines():
    x1, y1, x2, y2 = utils.extract_int('%-%,%-%', line)
    if (x1 <= x2 <= y1 and x1 <= y2 <= y1) or (x2 <= x1 <= y2 and x2 <= y1 <= y2):
        answer_1 += 1
    if x1 <= x2 <= y1 or x1 <= y2 <= y1 or x2 <= x1 <= y2 or x2 <= y1 <= y2:
        answer_2 += 1

print(f'Answer 1: {answer_1}')
print(f'Answer 2: {answer_2}')
