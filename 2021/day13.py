from aocd import get_data

raw = get_data(day=13, year=2021)
data = [n for n in raw.splitlines()]


def solve(lines):
    coordinates, folds = [], []
    max_x, max_y = 0, 0
    for line in lines:
        if not line.startswith('fold') and line:
            x, y = map(int, line.split(','))
            coordinates.append((x, y))
            max_x = x if x > max_x else max_x
            max_y = y if y > max_y else max_y
        elif line:
            folds.append((line.split('=')[0][-1], int(line.split('=')[1])))

    matrix = []
    for _ in range(max_y + 1):
        matrix.append([0 for _ in range(max_x + 1)])
    for x, y in coordinates:
        matrix[y][x] = 1

    for key, target in folds:
        target_y = len(matrix)
        target_x = len(matrix[0])
        if key == 'y':
            _y = target - 1
            for y in range(target + 1, target_y):
                for x in range(target_x):
                    if _y >= 0:
                        matrix[_y][x] |= matrix[y][x]
                _y -= 1
            matrix = matrix[:target]
        else:
            _x = target - 1
            for x in range(target + 1, target_x):
                for y in range(target_y):
                    if _x >= 0:
                        matrix[y][_x] |= matrix[y][x]
                _x -= 1
            matrix = [m[:target] for m in matrix]

        instruction = '\n'.join([''.join(['.' if each == 0 else '#' for each in row]) for row in matrix])
        print(f'({key},{target}) -> {instruction.count("#")}')
    return instruction


print(solve(data))
