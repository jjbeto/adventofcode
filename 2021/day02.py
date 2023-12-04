from aocd import get_data

raw = get_data(day=2, year=2021)

lines = [line.split(' ') for line in raw.splitlines()]


def part1(commands):
    horizontal, depth = 0, 0
    for command, move in commands:
        _move = int(move)
        if command == 'up':
            depth -= _move
        elif command == 'down':
            depth += _move
        elif command == 'forward':
            horizontal += _move
    return horizontal * depth


print(f'Answer 1: {part1(lines)}')


def part2(commands):
    horizontal, depth, aim = 0, 0, 0
    for command, move in commands:
        _move = int(move)
        if command == 'up':
            aim -= _move
        elif command == 'down':
            aim += _move
        elif command == 'forward':
            horizontal += _move
            depth += aim * _move
    return horizontal * depth


print(f'Answer 2: {part2(lines)}')
