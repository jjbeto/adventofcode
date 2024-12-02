from aocd import get_data

raw = get_data(day=2, year=2024)

reports = []
for line in list([line for line in raw.splitlines()]):
    strs = line.split(' ')
    reports.append([int(s) for s in strs])


def all_decrease_max_3(l: list):
    return all(l[x] > l[x + 1] and 0 < abs(l[x] - l[x + 1]) < 4 for x in range(len(l) - 1))


def all_increase_max_3(l: list):
    return all(l[x] < l[x + 1] and 0 < abs(l[x] - l[x + 1]) < 4 for x in range(len(l) - 1))


def part1():
    return sum([
        1 if all_increase_max_3(report) or all_decrease_max_3(report)
        else 0
        for report in reports
    ])


def tolerations(l: list):
    return [l[:i] + l[i + 1:] for i in range(len(l))]


def part2():
    return sum(
        1 if all_increase_max_3(report) or
             all_decrease_max_3(report) or
             any(all_increase_max_3(toletarion) or all_decrease_max_3(toletarion) for toletarion in tolerations(report))
        else 0
        for report in reports
    )


print(f'Answer 1: {part1()}')
# 566
print(f'Answer 2: {part2()}')
