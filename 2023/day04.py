from collections import defaultdict

from aocd import get_data

raw = get_data(day=4, year=2023).replace('  ', ' ')
total = 0
match = defaultdict(int)

for i, line in enumerate(raw.splitlines()):
    lists = line.split(': ')[1].split(' | ')
    winning, have = lists[0].split(' '), lists[1].split(' ')
    common = set(winning).intersection(have)
    match[i + 1] = len(common)
    if common:
        total += 2 ** (len(common) - 1)

pile = defaultdict(int)
for i, n in match.items():
    pile[i] += 1
    for copy in range(i + 1, i + 1 + n):
        pile[copy] += pile[i]

print(f'Answer 1: {total}')
print(f'Answer 2: {sum(pile.values())}')
