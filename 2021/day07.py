from aocd import get_data

raw = get_data(day=7, year=2021)


def part1(lines):
    counts = list(set((x, lines.count(x)) for x in lines))
    return min([sum(abs(x - target) * y for x, y in counts) for target in range(min(lines), max(lines))])


print(f"Answer 1: {part1(list([int(n) for n in raw.split(',')]))}")


def part2(lines):
    def total(n):
        return n * (n + 1) // 2

    counts = list(set((x, lines.count(x)) for x in lines))
    return min([
        sum(total(abs(x - target)) * y for x, y in counts)
        for target in range(min(lines), max(lines))
    ])


print(f"Answer 2: {part2(list([int(n) for n in raw.split(',')]))}")
