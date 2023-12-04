from collections import defaultdict

from aocd import get_data

raw = get_data(day=10, year=2020)

numbers = [int(n) for n in raw.splitlines()]
numbers = sorted(numbers + [0, max(numbers) + 3])

jolt_diff = defaultdict(int)
for i, n in enumerate(numbers):
    if i > 0:
        jolt_diff[n - numbers[i - 1]] += 1

print(f'Answer 1: {jolt_diff[1] * jolt_diff[3]}')


class Node:
    def __init__(self):
        self.parents = []
        self.children = []
        self.accum = 0


numbers = [int(n) for n in raw.splitlines()]
numbers = sorted(numbers + [0, max(numbers) + 3], reverse=True)
lines = len(numbers)
nodes = defaultdict(Node)


def add_relation(node, current_i, delta):
    if current_i + delta > lines - 1:
        return
    if numbers[current_i] <= numbers[current_i + delta] + 3:
        next_node = nodes[numbers[current_i + delta]]
        next_node.parents.append(node)
        node.children.append(next_node)


for i, n in enumerate(numbers):
    _node = nodes[n]
    add_relation(_node, i, +1)
    add_relation(_node, i, +2)
    add_relation(_node, i, +3)

nodes[max(numbers)].accum = 1
for _node in [nodes[n] for n in numbers]:
    for _parent in _node.parents:
        _node.accum += _parent.accum

print(f'Answer 2: {nodes[0].accum}')
