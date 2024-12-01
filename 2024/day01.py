from collections import Counter

from aocd import get_data

raw = get_data(day=1, year=2024)
col_a, col_b = [], []
for line in list([line for line in raw.splitlines()]):
    a, b = line.split('   ')
    col_a.append(int(a))
    col_b.append(int(b))

col_a.sort()
col_b.sort()


def part1():
    return sum([abs(a - col_b[i]) for i, a in enumerate(col_a)])


def part2():
    similarity = Counter(col_b)
    return sum([a * similarity.get(a, 0) for a in col_a])


print(f'Answer 1: {part1()}')
print(f'Answer 2: {part2()}')
