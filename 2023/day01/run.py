data = open('data.txt')
lines = [line for line in data.read().splitlines()]

calibrations = []


def to_digits(raw):
    for k, v in {
        'oneight': '18',
        'zerone': '01',
        'twone': '21',
        'nineight': '98',
        'threeight': '38',
        'fiveight': '58',
        'eightwo': '82',
        'eighthree': '83',
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'
    }.items():
        raw = raw.replace(k, v)
    return raw


for each in lines:
    line = to_digits(each)
    c1 = ''
    c2 = ''
    for c in line:
        if c.isnumeric():
            if c1 == '':
                c1 = c
            else:
                c2 = c
    if c2 == '':
        c2 = c1
    calibrations.append(int(c1 + c2))

print(f'Answer: {sum(calibrations)}')
