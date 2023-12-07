from aocd import get_data
from collections import Counter

raw = get_data(day=7, year=2023)
test = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

data = test

max_rank = len(data.splitlines())

hands, bids, rank = [], [], 0
for line in data.splitlines():
    val = line.split()
    hands.append(val[0]), bids.append(int(val[1]))
    rank += 1
    c = dict(Counter(val[0]))

print(f'Answer 2: {"solution2"}')
