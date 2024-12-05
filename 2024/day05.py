from collections import defaultdict

from aocd import get_data

raw = get_data(day=5, year=2024)

data = raw.split('\n\n')

must_before = defaultdict(set)
must_after = defaultdict(set)
for line in data[0].splitlines():
    rule = line.split('|')
    must_before[rule[1]].add(rule[0])
    must_after[rule[0]].add(rule[1])

valids = []
invalids = []
for line in data[1].splitlines():
    curr = line.split(',')
    allow = True
    for i, each in enumerate(curr):
        if i == 0 or i == len(curr) - 1:
            continue
        if any(curr in must_after[each] for curr in curr[:i]) or any(curr in must_before[each] for curr in curr[i + 1:]):
            allow = False
            break
    if allow:
        valids.append(curr)
    else:
        invalids.append(curr)


def part1():
    return sum(int(valid[len(valid) // 2]) for valid in valids)


def bubble_sort(seq):
    size = len(seq)
    for i in range(size):
        already_sorted = True
        for j in range(size - i - 1):
            if seq[j] in must_after[seq[j + 1]] or seq[j + 1] in must_before[seq[j]]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                already_sorted = False
        if already_sorted:
            break
    return seq


def part2():
    new_valids = [bubble_sort(invalid) for invalid in invalids]
    return sum(int(valid[len(valid) // 2]) for valid in new_valids)


print(f'Answer 1: {part1()}')
print(f'Answer 2: {part2()}')
