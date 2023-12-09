from aocd import get_data

raw = get_data(day=9, year=2023)


def extrapolate(line, reverse=False):
    col = []
    vals = list([int(i) for i in line.split()])
    while vals.count(0) != len(vals):
        col.append(vals[-1] if not reverse else vals[0])
        vals = [j - i for i, j in zip(vals[:-1], vals[1:])]
    s = 0
    for f in col[::-1]:
        s = f + s if not reverse else f - s
    return s


print(f'Answer 1: {sum([extrapolate(line, False) for line in raw.splitlines()])}')
print(f'Answer 2: {sum([extrapolate(line, True) for line in raw.splitlines()])}')
