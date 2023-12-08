import math

from aocd import get_data

import utils

raw = get_data(day=8, year=2023)
data = raw


def solve1():
    nodes = {}
    for line in data.splitlines()[2:]:
        src, left, right = utils.extract_string('% = (%, %)', line)
        nodes[src] = (left, right)

    loop = [int(s) for s in data.splitlines()[0].replace('L', '0').replace('R', '1')]
    steps, cur = 0, 'AAA'
    while cur != 'ZZZ':
        for direction in loop:
            cur = nodes[cur][direction]
            steps += 1
            if cur == 'ZZZ':
                break
    return steps


print(f'Answer 1: {solve1()}')


def solve2():
    nodes, starters = {}, []
    for line in data.splitlines()[2:]:
        src, left, right = utils.extract_string('% = (%, %)', line)
        nodes[src] = (left, right)
        if src[2] == 'A':
            starters.append(src)

    loop = [int(s) for s in data.splitlines()[0].replace('L', '0').replace('R', '1')]
    steps, cur = [0] * len(starters), starters
    while len([x for x in cur if x.endswith('Z')]) < len(cur):
        for i in range(len(cur)):
            count = 0
            while not cur[i].endswith('Z'):
                for direction in loop:
                    cur[i] = nodes[cur[i]][direction]
                    count += 1
                    if cur[i].endswith('Z'):
                        steps[i] = count
                        break

    return math.lcm(*steps)


print(f'Answer 2: {solve2()}')
