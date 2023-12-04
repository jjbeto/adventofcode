import re

from aocd import get_data

raw = get_data(day=4, year=2020)

lines = raw.split('\n\n')

passports = []
for line in lines:
    data = {}
    for pair in [raw.split(':') for raw in line.replace('\n', ' ').split(' ') if raw]:
        data[pair[0]] = pair[1]
    passports.append(data)

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
with_required = [each for each in passports if all(item in each.keys() for item in required)]

print(f'Answer 1: {len(with_required)}')

hgt = re.compile(r"^([1]([5-8][0-9]|[9][0-3])cm)$|^(([5][9]|[7][0-6]|[6][0-9])in)$")
hcl = re.compile(r"^#[0-9a-f]{6}$")


def valid_byr(v: str):
    return v.isnumeric() and 1920 <= int(v) <= 2002


def valid_iyr(v: str):
    return v.isnumeric() and 2010 <= int(v) <= 2020


def valid_eyr(v: str):
    return v.isnumeric() and 2020 <= int(v) <= 2030


def valid_hgt(v: str):
    return True if hgt.match(v) else False


def valid_hcl(v: str):
    return True if hcl.match(v) else False


def valid_ecl(v: str):
    return True if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else False


def valid_pid(v: str):
    return v.isnumeric() and len(v) == 9


valid = [each for each in with_required
         if valid_byr(each['byr'])
         and valid_iyr(each['iyr'])
         and valid_eyr(each['eyr'])
         and valid_hgt(each['hgt'])
         and valid_hcl(each['hcl'])
         and valid_ecl(each['ecl'])
         and valid_pid(each['pid'])]

print(f'Answer 2: {len(valid)}')
