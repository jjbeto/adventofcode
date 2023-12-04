from aocd import get_data

raw = get_data(day=13, year=2020)

data = raw.splitlines()
timestamp = int(data[0])
buses = [(i, int(each)) for i, each in enumerate(data[1].split(',')) if each != 'x']


def part_1():
    loop = timestamp
    while True:
        loop += 1
        for _, bus in buses:
            if loop % bus == 0:
                return (loop - timestamp) * bus


print(f'Answer 1: {part_1()}')


def part_2():
    delta = buses[0][1]
    loop = 0
    for i, bus in buses[1:]:
        while (loop + i) % bus != 0:
            loop += delta
        delta *= bus
    return loop


print(f'Answer 2: {part_2()}')
