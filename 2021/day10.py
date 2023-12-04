import queue

from aocd import get_data

raw = get_data(day=10, year=2021)

data = [n for n in raw.splitlines()]
mapping = {')': '(', ']': '[', '}': '{', '>': '<'}


def part1(lines):
    total = {')': 0, ']': 0, '}': 0, '>': 0}
    corrupted = []
    for i, line in enumerate(lines):
        chunks = queue.LifoQueue()
        for each in line:
            if each in mapping.values():
                chunks.put(each)
            else:
                if mapping[each] != chunks.get():
                    total[each] += 1
                    corrupted.append(i)
                    break
    return sum([total[')'] * 3, total[']'] * 57, total['}'] * 1197, total['>'] * 25137]), corrupted


p1, corrupted_d = part1(data)
print(f'Answer 1: {p1}')


def part2(lines, corrupted_indexes):
    autocomplete = []
    for line in [l for i, l in enumerate(lines) if i not in corrupted_indexes]:
        chunks = queue.LifoQueue()
        [chunks.put(each) if each in mapping.values() else chunks.get() for each in line]

        values = []
        while not chunks.empty():
            last = chunks.get()
            if last == '(':
                values.append(1)
            elif last == '[':
                values.append(2)
            elif last == '{':
                values.append(3)
            else:
                values.append(4)
        autocomplete.append(values)

    scores = []
    for line in autocomplete:
        score = 0
        for value in line:
            score = score * 5 + value
        scores.append(score)
    return sorted(scores)[len(scores) // 2]


p2 = part2(data, corrupted_d)
print(f'Answer 2: {p2}')
