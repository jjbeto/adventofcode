from aocd import get_data

raw = get_data(day=12, year=2023)


def solve(text, text_i, pos, pos_i, block_len, cache):
    key = (text_i, pos_i, block_len)
    if key in cache:
        return cache[key]
    if text_i == len(text):
        if (pos_i == len(pos) and block_len == 0) or (pos_i == len(pos) - 1 and pos[pos_i] == block_len):
            return 1
        else:
            return 0

    total = 0
    for c in '.#':
        if text[text_i] == c or text[text_i] == '?':
            if c == '.' and block_len == 0:
                total += solve(text, text_i + 1, pos, pos_i, 0, cache)
            elif c == '.' and block_len > 0 and pos_i < len(pos) and pos[pos_i] == block_len:
                total += solve(text, text_i + 1, pos, pos_i + 1, 0, cache)
            elif c == '#':
                total += solve(text, text_i + 1, pos, pos_i, block_len + 1, cache)
    cache[key] = total
    return total


def score(part2):
    total = 0
    for line in raw.splitlines():
        text, pos = line.split()
        if part2:
            text = '?'.join([text, text, text, text, text])
            pos = ','.join([pos, pos, pos, pos, pos])
        pos = [int(x) for x in pos.split(',')]
        total += solve(text, 0, pos, 0, 0, dict())
    return total


print(f'Answer 1: {score(False)}')
print(f'Answer 2: {score(True)}')
