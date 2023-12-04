from aocd import get_data

raw = get_data(day=16, year=2021)


def parser(binary, track_version=[]):
    version = int(binary[0:3], 2)
    track_version.append(version)
    type_id = int(binary[3:6], 2)
    if type_id == 4:
        chunks, chunk, n = '', binary[6:11], 11
        while True:
            chunks += chunk[1:]
            if chunk.startswith('0'):
                break
            chunk = binary[n:n + 5]
            n += 5
        remaining = binary[n:] if binary[n:] and int(binary[n:], 2) > 0 else None
        value = int(chunks, 2)
    else:
        if binary[6:7] == '0':
            length = int(binary[7:7 + 15], 2)
            sub_pack_bin = binary[7 + 15:7 + 15 + length]
            chunk, sub_remaining = parser(sub_pack_bin, track_version)
            value = [chunk]
            while sub_remaining:
                chunk, sub_remaining = parser(sub_remaining, track_version)
                value.append(chunk)
            remaining = binary[7 + 15 + length:]
        else:
            length = int(binary[7:7 + 11], 2)
            chunk, remaining = parser(binary[7 + 11:], track_version)
            value = [chunk]
            while len(value) < length:
                chunk, remaining = parser(remaining, track_version)
                value.append(chunk)

    return (version, type_id, value), remaining


def part1(text):
    binary = bin(int('1' + text, 16))[3:]
    track_version = []
    chunks, _ = parser(binary, track_version)
    return sum(track_version)


print(f'Answer 1: {part1(raw)}')

import math


def execute(chunk):
    _, t, val = chunk
    if t == 4:
        return val
    if type(val) == list:
        val = [execute(v) for v in val]
    if t == 0:
        return sum(val)
    if t == 1:
        return math.prod(val)
    if t == 2:
        return min(val)
    if t == 3:
        return max(val)
    if t == 5:
        return 1 if val[0] > val[1] else 0
    if t == 6:
        return 1 if val[0] < val[1] else 0
    if t == 7:
        return 1 if val[0] == val[1] else 0


def part2(text):
    binary = bin(int('1' + text, 16))[3:]
    chunks, _ = parser(binary)
    return execute(chunks)


print(f'Answer 2: {part2(raw)}')
