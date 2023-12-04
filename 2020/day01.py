from aocd import get_data

raw = get_data(day=1, year=2020)

numbers = list([int(n) for n in raw.splitlines()])
numbers.sort()


def find_2_sum():
    for a in range(len(numbers) - 1):
        for b in range(a + 1, len(numbers)):
            if numbers[a] + numbers[b] == 2020:
                return numbers[a], numbers[b]
    return None, None


x, y = find_2_sum()
print(f'Answer 1: {x * y}')


def find_3_sum():
    for a in range(len(numbers) - 2):
        for b in range(a + 1, len(numbers) - 1):
            for c in range(b + 1, len(numbers)):
                if numbers[a] + numbers[b] + numbers[c] == 2020:
                    return numbers[a], numbers[b], numbers[c]
    return None, None, None


x, y, z = find_3_sum()
print(f'Answer 2: {x * y * z}')
