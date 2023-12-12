from aocd import get_data

import utils

raw = get_data(day=11, year=2023)


def solve(text, distance):
    x_spaces = [x for x, line in enumerate(text.splitlines()) if line.count(line[0]) == len(line)]

    rotated = utils.matrix_to_text(
        utils.rotate_matrix_clockwise(
            utils.text_to_matrix(text)
        )
    )
    y_spaces = [y for y, line in enumerate(rotated.splitlines()) if line.count(line[0]) == len(line)]

    vec, x = set(), 0
    for _x in range(len(text.splitlines())):
        x += distance - 1 if _x in x_spaces else 0
        y = 0
        for _y in range(len(text.splitlines()[0])):
            y += distance - 1 if _y in y_spaces else 0
            if text.splitlines()[_x][_y] == "#":
                vec.add((x + _x, y + _y))

    vec, total = list(vec), 0
    for _x in range(len(vec)):
        for _y in range(_x + 1, len(vec)):
            total += abs(vec[_x][0] - vec[_y][0]) + abs(vec[_x][1] - vec[_y][1])
    return total


print(f'Answer 1: {solve(raw, 2)}')
print(f'Answer 2: {solve(raw, 1_000_000)}')
