from aocd import get_data

raw = get_data(day=3, year=2021)

lines = list([n for n in raw.splitlines()])
n_cols = len(lines[0])


def to_columns(_lines):
    columns = []
    n_lines = len(_lines)
    for c in range(n_cols):
        columns.append('')
        for i in range(n_lines):
            columns[c] += _lines[i][c]
    return columns, n_lines


def part1():
    gama, epsilon = '', ''
    columns, n_lines = to_columns(lines)
    for col in columns:
        if col.count('1') > n_lines / 2:
            gama += '1'
            epsilon += '0'
        else:
            gama += '0'
            epsilon += '1'
    gama = int(gama, 2)
    epsilon = int(epsilon, 2)
    return gama * epsilon


print(f'Answer 1: {part1()}')


def rating(param):
    filtered = lines.copy()
    prefix = ''
    for i in range(n_cols):
        columns, n_lines = to_columns(filtered)
        if param == 'oxygen':
            prefix += '1' if columns[i].count('1') >= n_lines / 2 else '0'
        elif param == 'co2':
            prefix += '0' if columns[i].count('0') <= n_lines / 2 else '1'
        filtered = [f for f in filtered if f.startswith(prefix)]
        if len(filtered) == 1:
            break
    return int(filtered[0], 2)


def part2():
    return rating("oxygen") * rating("co2")


print(f'Answer 2: {part2()}')
