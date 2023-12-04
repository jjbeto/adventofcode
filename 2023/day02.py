from aocd import get_data

raw = get_data(day=2, year=2023)


def solution1(data):
    total = 0
    for i, line in enumerate(data.splitlines()):
        games = [g.split(', ') for g in line.split(': ')[1].split('; ')]
        possible = True
        for game in games:
            for g in [_g.split(' ') for _g in game]:
                k, v = g[1], int(g[0])
                possible = (k == 'red' and v <= 12) or (k == 'green' and v <= 13) or (k == 'blue' and v <= 14)
                if not possible:
                    break
            else:
                continue
            break
        if possible:
            total += int(i) + 1
    return total


print(f'Answer 1: {solution1(raw)}')


def solution2(data):
    total = 0
    for line in data.splitlines():
        games = [g.split(', ') for g in line.split(': ')[1].split('; ')]
        r, g, b = 0, 0, 0
        for game in games:
            for e in [_g.split(' ') for _g in game]:
                k, v = e[1], int(e[0])
                if k == 'red' and v > r:
                    r = v
                elif k == 'green' and v > g:
                    g = v
                elif k == 'blue' and v > b:
                    b = v
        total += r * g * b
    return total


print(f'Answer 2: {solution2(raw)}')
