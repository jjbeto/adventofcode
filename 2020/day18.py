from aocd import get_data

raw = get_data(day=18, year=2020)


class P1:
    def __init__(self, val): self.val = int(val)

    def __add__(self, other): return P1(self.val + other.val)

    def __sub__(self, other): return P1(self.val * other.val)

    def __repr__(self): return f'P1({self.val})'


def part_1(expression: str):
    return eval(''.join(f'P1({each})' if each.isnumeric() else each for each in expression.replace('*', '-')))


print(part_1('1 + 2 * 3 + 4 * 5 + 6'), 71)
print(part_1('1 + (2 * 3) + (4 * (5 + 6))'), 51)
print(part_1('2 * 3 + (4 * 5)'), 26)
print(part_1('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 437)
print(part_1('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 12240)
print(part_1('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 13632)

answer_1 = sum([part_1(line).val for line in raw.splitlines()])
print(f"Answer 1: {answer_1}")


class P2:
    def __init__(self, val): self.val = int(val)

    def __sub__(self, other): return P2(self.val * other.val)

    def __truediv__(self, other): return P2(self.val + other.val)

    def __repr__(self): return f'P2({self.val})'


def part_2(expression: str):
    return eval(''.join(f'P2({each})' if each.isnumeric() else each
                        for each in expression.replace('*', '-').replace('+', '/')))


print(part_2('1 + 2 * 3 + 4 * 5 + 6'), 231)
print(part_2('1 + (2 * 3) + (4 * (5 + 6))'), 51)
print(part_2('2 * 3 + (4 * 5)'), 46)
print(part_2('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 1445)
print(part_2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 669060)

answer_2 = sum([part_2(line).val for line in raw.splitlines()])
print(f"Answer 2: {answer_2}")
