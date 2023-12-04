from aocd import get_data

raw = get_data(day=6, year=2021)


def part1(spawn, days):
    spawn = [int(c) for c in spawn]
    for d in range(days):
        zeros = spawn.count(0)
        spawn = [6 if x == 0 else x - 1 for x in spawn]
        if zeros:
            spawn += [8] * zeros
    return len(spawn)


print(f"Answer 1: {part1(raw.replace(',', ''), 80)}")


def part2(spawn, days):
    _spawn = [0] * 9
    for s in [int(c) for c in spawn]:
        _spawn[s] += 1

    def increase():
        _new = _spawn.pop(0)
        _spawn[6] += _new
        _spawn.append(_new)

    [increase() for _ in range(days)]
    return sum(_spawn)


print(f"Answer 2: {part2(raw.replace(',', ''), 256)}")
