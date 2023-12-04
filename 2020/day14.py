from collections import defaultdict

from aocd import get_data

raw = get_data(day=14, year=2020)
lines = raw.splitlines()


def part_1():
    memory = defaultdict(int)
    for line in lines:
        command = line.split(' = ')
        if command[0] == 'mask':
            mask = command[1]
            continue

        value = bin(int(command[1])).replace("0b", "").zfill(len(mask))  # convert to binary and fill zeros
        value_masked = ''.join([bitmask if bitmask != 'X' else value[i] for i, bitmask in enumerate(mask)])

        address = int(command[0][command[0].find('[') + 1:command[0].find(']')])
        memory[address] = int(value_masked, 2)
    return sum(memory.values())


print(f'Answer 1: {part_1()}')

from itertools import product


def part_2():
    memory = defaultdict(int)
    for line in lines:
        command = line.split(' = ')
        if command[0] == 'mask':
            mask = command[1]
            continue

        address = int(command[0][command[0].find('[') + 1:command[0].find(']')])
        address = bin(int(address)).replace("0b", "").zfill(len(mask))  # convert to binary and fill zeros
        address_masked = ''.join([address[i] if bitmask == '0' else '{}' if bitmask == 'X' else bitmask
                                  for i, bitmask in enumerate(mask)])

        value = int(command[1])
        for _address in [address_masked.format(*arrange) for arrange in list(product([0, 1], repeat=mask.count('X')))]:
            memory[int(_address, 2)] = value
    return sum(memory.values())


print(f'Answer 2: {part_2()}')
