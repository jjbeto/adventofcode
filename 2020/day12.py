from aocd import get_data

raw = get_data(day=12, year=2020)

lines = raw.splitlines()
factor_x = {'E': +1, 'W': -1}
factor_y = {'N': +1, 'S': -1}


def part_1():
    ship_x, ship_y = 0, 0
    facing_x, facing_y = 1, 0
    for action, n in [(line[0], int(line[1:])) for line in lines]:
        if action in factor_x:
            ship_x += n * factor_x[action]
        elif action in factor_y:
            ship_y += n * factor_y[action]
        elif action == 'F':
            ship_x += n * facing_x
            ship_y += n * facing_y
        else:
            for _ in range(n // 90):
                facing_x, facing_y = (-facing_y, facing_x) if action == 'L' else (facing_y, -facing_x)

    return abs(ship_x) + abs(ship_y)


print(f'Answer 1: {part_1()}')


def part_2():
    ship_x, ship_y = 0, 0
    waypoint_x, waypoint_y = 10, 1
    for action, n in [(line[0], int(line[1:])) for line in lines]:
        if action in factor_x:
            waypoint_x += n * factor_x[action]
        elif action in factor_y:
            waypoint_y += n * factor_y[action]
        elif action == 'F':
            ship_x += n * waypoint_x
            ship_y += n * waypoint_y
        else:
            for _ in range(n // 90):
                waypoint_x, waypoint_y = (-waypoint_y, waypoint_x) if action == 'L' else (waypoint_y, -waypoint_x)

    return abs(ship_x) + abs(ship_y)


print(f'Answer 2: {part_2()}')
