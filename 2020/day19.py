import regex
from aocd import get_data

raw = get_data(day=19, year=2020)


class Solution:

    def __init__(self, input_text):
        _rules = input_text.split('\n\n')[0]
        self.rules = sorted([(int(_r.split(': ')[0]), _r.split(': ')[1].replace('"', ''))
                             for _r in _rules.splitlines()], key=lambda e: e[0])
        self.messages = input_text.split('\n\n')[1].split('\n')
        _regex = str(self.load_data(0)) \
            .replace('\'', '') \
            .replace('[', '(') \
            .replace(']', ')') \
            .replace(', ', '') \
            .replace('"', '')
        self.matcher = regex.compile(f'^{_regex}$')

    def load_data(self, i):
        rule = next(_r for _r in self.rules if _r[0] == i)[1].split(' ')
        data = []
        for _i, each in enumerate(rule):
            if each.isdigit() and each != f'{i}':
                data.append(self.load_data(int(each)))
            # (!) next `if` solves part2
            elif each == f'{i}':
                if each == '8':
                    data.append([self.load_data(42), '+'])
                elif each == '11':
                    left, right = self.load_data(42), self.load_data(31)
                    data.append(f'(?P<hacky>{left}(?P>hacky)?{right})')
            else:
                data.append(each)
        return f"({''.join(data)})" if all(isinstance(item, str) and len(item) == 1 for item in data) else data

    def count(self):
        return sum([1 if self.matcher.match(message) else 0 for message in self.messages])


print(f"Answer 1: {Solution(raw).count()}")
print(f"Answer 2: {Solution(raw.replace('8: 42', '8: 42 | 42 8').replace('11: 42 31', '11: 42 31 | 42 11 31')).count()}")
