from aocd import get_data

raw = get_data(day=6, year=2020)

lines = raw.split('\n\n')

acceptable = 'abcdefghijklmnopqrstuvwxyz'
groups = [len(set([letter for letter in line if letter in acceptable])) for line in lines]
print(f'Answer 1: {sum(groups)}')

everyone_yes = []
for line in lines:
    group = line.split()
    result = set(group[0])
    for person in group[1:]:
        result = [letter for letter in result if letter in person]
    everyone_yes.append(len(result))
print(f'Answer 2: {sum(everyone_yes)}')
