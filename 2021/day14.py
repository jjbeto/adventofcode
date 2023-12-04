from collections import Counter

from aocd import get_data

raw = get_data(day=14, year=2021)
data = [n for n in raw.splitlines()]


def solve(lines, steps):
    template = lines[0]
    rules = {lines[i].split(' -> ')[0]: lines[i].split(' -> ')[1] for i in range(2, len(lines))}

    char_count = Counter(template)
    pair_count = Counter(template[i:i + 2] for i in range(len(template) - 1))

    for step in range(steps):
        new_count = Counter()
        for pair, num in pair_count.items():
            if pair in rules:
                x, y = pair
                c = rules[pair]
                new_count[x + c] += num
                new_count[c + y] += num
                char_count[c] += num
            else:
                new_count[pair] = num
        pair_count = new_count

    return max(char_count.values()) - min(char_count.values())


print(f'Answer 1: {solve(data, 10)}')
print(f'Answer 2: {solve(data, 40)}')
