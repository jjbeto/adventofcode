import re

from aocd import get_data

raw = get_data(day=3, year=2024)


def part1():
    total = 0
    for each in re.findall(r'(mul\(\d{1,3},\d{1,3}\))', raw):
        ab = each.replace('mul(', '').replace(')', '').split(',')
        total += int(ab[0]) * int(ab[1])
    return total


def part2():
    do = True
    total = 0
    for each in re.findall(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', raw):
        if each == 'do()':
            do = True
        elif each == "don't()":
            do = False
        elif do:
            ab = each.replace('mul(', '').replace(')', '').split(',')
            total += int(ab[0]) * int(ab[1])
    return total


print(f'Answer 1: {part1()}')
print(f'Answer 2: {part2()}')
