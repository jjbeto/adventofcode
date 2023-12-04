from aocd import get_data

raw = get_data(day=18, year=2021)


def map_text(text):
    _cur, _max, _index = 0, 0, -1
    numbers = {}
    for i in range(len(text)):
        if text[i] == '[':
            _cur += 1
            if _cur > _max:
                _max = _cur
                _index = i
        elif text[i] == ']':
            _cur -= 1
        elif text[i].isnumeric():
            if i - 1 in numbers:
                numbers[i - 1] = int(f'{numbers[i - 1]}{text[i]}')
            else:
                numbers[i] = int(text[i])
    return _max, _index, numbers


def explode(text, _max, _index, _numbers):
    _index_end = text.find(']', _index)
    x, y = map(int, text[_index + 1:_index_end].split(','))

    def __change(_target, _delta):
        _len = len(f'{_numbers[_target]}')
        _new = _numbers[_target] + _delta
        return f'{text[:_target]}{_new}{text[_target + _len:]}'

    right = min([n for n in _numbers.keys() if n > _index_end], default=None)
    text = __change(right, y) if right is not None else text

    left = max([n for n in _numbers.keys() if n < _index], default=None)
    text = __change(left, x) if left is not None else text

    diff = len(f'{_numbers[left] + x}') - len(f'{_numbers[left]}') if left else 0

    return f'{text[:_index + diff]}0{text[_index_end + 1 + diff:]}'


def split(text, _numbers):
    for i, v in ((_i, _v) for _i, _v in _numbers.items() if _v > 9):
        _len = len(f'{v}')
        return f'{text[:i]}[{v // 2},{(v // 2) + (v % 2)}]{text[i + _len:]}'


def magnitude(value):
    _listing = []
    if isinstance(value, str):
        exec(f'_listing.append({value})')
        _listing = _listing[0]
    elif isinstance(value, int):
        return value
    else:
        _listing = value

    return 3 * magnitude(_listing[0]) + 2 * magnitude(_listing[1])


def calculate(text):
    while True:
        _max, _index, _numbers = map_text(text)
        if _max > 4:
            text = explode(text, _max, _index, _numbers)
        elif max(_numbers.values()) > 9:
            text = split(text, _numbers)
        else:
            return text


def part1(lines):
    text = calculate(f'[{lines[0]},{lines[1]}]')
    if len(lines) > 2:
        for i in range(2, len(lines)):
            text = calculate(f'[{text},{lines[i]}]')
    return magnitude(text)


data = [n for n in raw.splitlines()]
print(f'Answer 1: {part1(data)}')


def part2(lines):
    magnitudes = {}
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j:
                continue
            magnitudes[(i, j)] = part1([lines[i], lines[j]])
    return max(magnitudes.values())


print(f'Answer 2: {part2(data)}')
