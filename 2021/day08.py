from aocd import get_data

raw = get_data(day=8, year=2021)


def part1(lines):
    display = []
    for line in lines:
        [display.append(d) for d in line.split(' | ')[1].split(' ') if len(d) in [2, 4, 3, 7]]
    return len(display)


print(f"Answer 1: {part1(list([n for n in raw.splitlines()]))}")


def part2(lines):
    lines = [line for line in lines]
    displays = []
    for line in lines:
        unknown = []
        known = [None] * 10
        for each in line.split(' | ')[0].split(' '):
            val, size = set(each), len(each)
            if size == 2:
                known[1] = val
            elif size == 4:
                known[4] = val
            elif size == 3:
                known[7] = val
            else:
                unknown.append(val)

        known[8] = set('abcdefg')

        for u in [_u for _u in unknown if len(_u) == 5]:
            if known[7].issubset(u):
                known[3] = u
            else:
                remain = u - known[4]
                if len(remain) == 2:
                    known[5] = u
                else:
                    known[2] = u

        for u in [_u for _u in unknown if len(_u) == 6]:
            if not known[7].issubset(u):
                known[6] = u
            elif known[3].issubset(u):
                known[9] = u
            else:
                known[0] = u

        outputs = [known.index(set(each)) for each in line.split(' | ')[1].split(' ')]
        displays.append(int(''.join([str(i) for i in outputs])))
    return sum(displays)


print(f"Answer 2: {part2(list([n for n in raw.splitlines()]))}")
