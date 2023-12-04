from queue import PriorityQueue

from aocd import get_data

raw = get_data(day=1, year=2022)

q = PriorityQueue()
curr = 0
for line in raw.splitlines():
    if line == '':
        q.put(curr)
        curr = 0
        continue
    curr -= int(line)

_1st = -q.get()
_2nd = -q.get()
_3rd = -q.get()

print(f'Answer 1: {_1st}')
print(f'Answer 2: {_1st + _2nd + _3rd}')
