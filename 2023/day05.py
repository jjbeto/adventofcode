from aocd import get_data

raw = get_data(day=5, year=2023)
seeds = [int(seed) for seed in raw.splitlines()[0].replace('seeds: ', '').split()]


def solution1():
    location = float('inf')
    for n in seeds:
        found = False
        for line in raw.splitlines()[1:]:
            if line == '':
                found = False
                continue
            if found or not line[0].isnumeric():
                continue
            dst, src, steps = [int(x) for x in line.split()]
            if src <= n < src + steps:
                n = dst + n - src
                found = True
        if n < location:
            location = n
    return location


print(f'Answer 1: {solution1()}')


def solution2():
    almanac = [line.splitlines() for line in raw.split('\n\n')]
    ranges = list([[seeds[i], seeds[i] + seeds[i + 1] - 1] for i in range(0, len(seeds), 2)])
    for mapping in almanac[1:]:
        i = 0
        while i < len(ranges):
            r1, r2 = ranges[i]
            for line in mapping[1:]:
                dst, src, steps = [int(x) for x in line.split()]
                if src <= r1 < src + steps:
                    ranges[i][0] = dst + r1 - src
                    if r2 < src + steps:
                        ranges[i][1] = dst + r2 - src
                    else:
                        ranges[i][1] = dst + steps - 1
                        ranges.append([src + steps, r2])
                elif src <= r2 < src + steps:
                    ranges[i][1] = dst + (r2 - src)
                    if r1 > src:
                        ranges[i][0] = dst + (r1 - src)
                    else:
                        ranges[i][0] = dst
                        ranges.append([r1, src - 1])
            i += 1
    return min(s for s in ranges)


print(f'Answer 2: {solution2()[0]}')
