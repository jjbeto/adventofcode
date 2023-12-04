from aocd import get_data

raw = get_data(day=16, year=2020)

blocks = raw.split('\n\n')
accepted = {}
for line in [_l for _l in blocks[0].split('\n')]:
    """Transforms 2 ranges into a flat list of integer: 1-2 or 4-6 -> [1, 2, 4, 5, 6]"""
    data = line.split(': ')
    accepted[data[0]] = sum(((list(range(*[int(n) + i for i, n in enumerate(_range.split('-'))])))
                             for _range in data[1].split(' or ')), [])


def find_error(ticket: str):
    for number in [int(n) for n in ticket.split(',')]:
        if not any(number in acceptable for acceptable in accepted.values()):
            return number
    return None


tickets = list([(line, find_error(line)) for line in [_l for _l in blocks[2].split('\n')[1:]]])
part_1 = sum([t[1] for t in tickets if t[1]])

print(f"Answer 1: {part_1}")


def part_2():
    """associate all positions to all fields"""
    positions = {k: list([i for i in range(len(accepted))]) for k in accepted}  # initially all is accepted
    for valid in [t[0] for t in tickets if t[1] is None]:
        for i, value in enumerate([int(n) for n in valid.split(',')]):
            [positions[field].remove(i) for field, acceptable in accepted.items() if value not in acceptable]

    """remove positions that do not fit by rule on each field"""
    used_positions = set()
    fields = {}
    for field, values in sorted(positions.items(), key=lambda entry: len(entry[1])):  # sort by number of positions
        for position in [_p for _p in values if _p not in used_positions]:
            fields[position] = field
            used_positions.add(position)

    """multiply just the encountered fields that starts with 'departure'"""
    departure_data = 1
    for position, field in [(_p, _f) for _p, _f in fields.items() if _f.startswith('departure')]:
        departure_data *= next(int(each) for i, each in enumerate(blocks[1].split(',')) if i == position)

    return departure_data


print(f"Answer 2: {part_2()}")
