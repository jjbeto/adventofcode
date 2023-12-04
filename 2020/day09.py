from itertools import combinations

from aocd import get_data

raw = get_data(day=9, year=2020)

numbers = [int(n) for n in raw.splitlines()]
preamble = 25

target = None
for index in range(preamble, len(numbers)):
    target = numbers[index]
    _preamble_set = set(numbers[index - preamble:index])
    _possibilities = [p for p in _preamble_set if abs(target - p) in _preamble_set]
    _combinations = list(combinations(_possibilities, 2))
    if not any([sum(pair) == target for pair in _combinations]):
        break

print(f'Answer 1: {target}')


def find_weakness_v1():
    subset = []
    for n in numbers:
        subset.append(n)
        while sum(subset) > target:
            subset.pop(0)
        if sum(subset) == target:
            break
    return min(subset) + max(subset)


print(f'Answer 2: {find_weakness_v1()}')


# Then discussing with [cmears](https://gitlab.com/cmears) he gave me a nice idea for linear execution for part 2.
# And thx to [GoossensMichael](https://github.com/GoossensMichael) for review!

def find_weakness_v2():
    subset = []
    subtotal = 0
    for n in numbers:
        subset.append(n)
        subtotal += n
        if subtotal > target:
            removed = 0
            for _ in subset:
                removed += subset.pop(0)
                if subtotal - removed <= target:
                    break
            subtotal -= removed
        if subtotal == target:
            break
    return min(subset) + max(subset)


print(f'Answer 2 v2: {find_weakness_v2()}')
