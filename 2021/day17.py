def launch(x, y, max_x, min_x, max_y, min_y):
    _x, _y, _max = x, y, 0
    while True:
        _max = _y if _y > _max else _max
        if max_x >= _x >= min_x and min_y <= _y <= max_y:
            return True, _max  # reached
        if _y < min_y:
            return False, _max  # pass through
        x += 1 if x < 0 else -1 if x > 0 else 0
        y -= 1
        _x, _y = _x + x, _y + y


def solve(max_x, min_x, max_y, min_y):
    velocity = {}
    for x in range(1, max_x + 1):
        for y in range(min_y, abs(min_y) + 1):
            _reached, _max = launch(x, y, max_x, min_x, max_y, min_y)
            if _reached:
                velocity[(x, y)] = _max

    return max(velocity.values()), len(velocity)


m, v = solve(max_x=215, min_x=155, max_y=-72, min_y=-132)
print(f'Answer 1: {m}')
print(f'Answer 2: {v}')
