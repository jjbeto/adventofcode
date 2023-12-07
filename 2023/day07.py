from collections import Counter
from queue import PriorityQueue

from aocd import get_data

raw = get_data(day=7, year=2023)

replacements1 = {
    '2': 'a', '3': 'b', '4': 'c', '5': 'd', '6': 'e', '7': 'f', '8': 'g', '9': 'h',
    'T': 'i', 'J': 'j', 'Q': 'k', 'K': 'l', 'A': 'm',
}
replacements2 = {
    'J': 'a',
    '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
    'T': 'j', 'Q': 'k', 'K': 'l', 'A': 'm',
}


def strength(hand, joker=''):
    if joker:
        n = dict(Counter(joker))
    else:
        n = dict(Counter(hand))
    _max, _min, _len = max(n.values()), min(n.values()), len(n.values())
    s = 0
    if _max == 1:  # High card
        s = 1
    elif _max == 2 and _len == 4:  # One pair
        s = 2
    elif _max == 2:  # Two pair
        s = 3
    elif _max == 3 and _min == 1:  # Three of a kind
        s = 4
    elif _max == 3 and _min == 2:  # Full house
        s = 5
    elif _max == 4:  # Four of a kind
        s = 6
    elif _max == 5:  # Five of a kind
        s = 7

    if joker:
        replacements = replacements2
    else:
        replacements = replacements1
    _hand = ''.join([replacements.get(c, c) for c in hand])
    return f'{s}_{_hand}'


def solve(is_joker):
    games = PriorityQueue()
    for line in raw.splitlines():
        val = line.split()
        if not is_joker:
            s = strength(val[0])
        elif val[0] == 'JJJJJ' or 'J' not in val[0]:
            s = strength(val[0], val[0])
        else:
            possibilities = []
            for c in dict(Counter(val[0])):
                if c == 'J':
                    continue
                possibilities.append(strength(val[0], val[0].replace('J', c)))
            ss = sorted(possibilities)
            s = ss[-1]
        games.put((s, int(val[1])))
    i = 1
    total = 0
    while not games.empty():
        g = games.get()
        total += i * g[1]
        i += 1
    return total


print(f'Answer 1: {solve(False)}')
print(f'Answer 2: {solve(True)}')
