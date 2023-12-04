from aocd import get_data

raw = get_data(day=1, year=2021)

numbers = list([int(n) for n in raw.splitlines()])


def increases(seq):
    return sum(1 for n in range(len(seq) - 1) if seq[n + 1] > seq[n])


print(f'Answer 1: {increases(numbers)}')

rolling = [sum(numbers[i:i + 3]) for i in range(len(numbers) - (3 - 1))]
print(f'Answer 2: {increases(rolling)}')
