from aocd import get_data

from utils import get_diagonals_from_text, reverse_text, get_columns_from_text

raw = get_data(day=4, year=2024)


def part1():
    lines = raw.splitlines()
    columns = get_columns_from_text(raw)
    diagonals_l_to_r = get_diagonals_from_text(raw)
    diagonals_r_to_l = get_diagonals_from_text(reverse_text(raw))

    possibilities = lines + columns + diagonals_l_to_r + diagonals_r_to_l
    possibilities = (
            [each for each in possibilities if len(each) > 3]
            + [each[::-1] for each in possibilities if len(each) > 3]  # all reversed
    )

    return sum(each.count('XMAS') for each in possibilities)


def part2():
    total = 0
    lines = raw.splitlines()
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines) - 1):
            if lines[y][x] != 'A':
                continue
            """
            M.S  ->  (x-1,y-1)     (x+1,y-1)  ->  a  _  b
            .A.  ->           (x,y)           ->  _ 'A' _
            M.S  ->  (x-1,y+1)     (x+1,y+1)  ->  c  _  d
            """
            a, b, c, d = lines[y - 1][x - 1], lines[y - 1][x + 1], lines[y + 1][x - 1], lines[y + 1][x + 1]
            if 'X' in [a, b, c, d] or 'A' in [a, b, c, d] or a == d or b == c:
                continue
            total += 1
    return total


print(f'Answer 1: {part1()}')
print(f'Answer 2: {part2()}')
