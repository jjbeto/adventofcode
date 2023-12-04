from aocd import get_data

import utils

raw = get_data(day=1, year=2023)


def calibration(data):
    total = 0
    for line in data.splitlines():
        first = utils.first_numeric(line)
        last = utils.first_numeric(line[::-1])
        total += int(first + last)
    return total


def to_digits(data):
    dictionary = {
        'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e',
        'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e', 'zero': 'z0o'
    }
    for k, v in dictionary.items():
        data = data.replace(k, v)
    return data


print(f'Answer 1: {calibration(raw)}')
print(f'Answer 2: {calibration(to_digits(raw))}')
