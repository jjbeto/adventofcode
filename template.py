test = list([n for n in open('dayXX.test').read().splitlines()])
data = list([n for n in open('dayXX.data').read().splitlines()])


def part1(lines):
    return 0


p1 = part1(test)
print(f'test1: {p1} - {p1 == 1}')
p1 = part1(data)
print(f'real1: {p1} - {p1 == 1}')


def part2(lines):
    return 0


p2 = part2(test)
print(f'test1: {p2} - {p2 == 1}')
p2 = part2(data)
print(f'part2: {p2} - {p2 == 1}')
