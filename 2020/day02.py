import re

from aocd import get_data

raw = get_data(day=2, year=2020)

pattern = re.compile(r"^(\d+)-(\d+) (\w): (\w+)$")
lines = raw.splitlines()

passwords_accepted = 0
for line in lines:
    matching = pattern.match(line)
    if matching:
        minimum, maximum, allowed_char, password = matching.groups()
        if int(minimum) <= password.count(allowed_char) <= int(maximum):
            passwords_accepted += 1

print(f'Answer 1: {passwords_accepted}')

passwords_accepted = 0
for line in lines:
    matching = pattern.match(line)
    if matching:
        pos1, pos2, allowed_char, password = matching.groups()
        on_pos1 = password[int(pos1) - 1] == allowed_char
        on_pos2 = password[int(pos2) - 1] == allowed_char
        if (on_pos1 and not on_pos2) or (not on_pos1 and on_pos2):
            passwords_accepted += 1

print(f'Answer 2: {passwords_accepted}')
