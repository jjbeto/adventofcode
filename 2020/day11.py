import copy

from aocd import get_data

raw = get_data(day=11, year=2020)

lines = open('day11.data').read().splitlines()
number_of_rows = len(lines)
number_of_cols = len(lines[0])


def printer(seat_map):
    [print(''.join([seat for seat in seat_row.values()])) for seat_row in seat_map]
    print('')


def occupied_surrounds_v1(seat_map, i, j):
    occupied_seats = 0
    for delta_i in [-1, 0, 1]:
        if i + delta_i >= number_of_rows or i + delta_i < 0:
            continue
        for delta_j in [-1, 0, 1]:
            if (delta_i, delta_j) != (0, 0):
                occupied_seats += 1 if seat_map[i + delta_i].get(j + delta_j, '.') == '#' else 0
    return occupied_seats


def load_passengers(occupied_check_method, occupied_limit=4, report=False):
    current_map = [dict(enumerate(row)) for row in lines]
    target_map = copy.deepcopy(current_map)

    changing_spots = True
    while changing_spots:
        if report:
            printer(target_map)
        changing_spots = False
        for i, row in enumerate(current_map):
            for j, col in row.items():
                current = current_map[i].get(j, '.')
                if current == 'L' and not occupied_check_method(current_map, i, j):
                    target_map[i][j] = '#'
                    changing_spots = True
                elif current == '#' and occupied_check_method(current_map, i, j) >= occupied_limit:
                    target_map[i][j] = 'L'
                    changing_spots = True
        current_map = copy.deepcopy(target_map)

    count = 0
    for row in current_map:
        for spot in row.values():
            if spot == '#':
                count += 1
    return count


print(f'Answer 1: {load_passengers(occupied_surrounds_v1)}')


def occupied_surrounds_v2(seat_map, i, j):
    occupied_seats = 0
    for delta_i in [-1, 0, 1]:
        if i + delta_i >= number_of_rows or i + delta_i < 0:
            continue
        for delta_j in [-1, 0, 1]:
            if (delta_i, delta_j) == (0, 0):
                continue
            next_i = i + delta_i
            next_j = j + delta_j
            spot = seat_map[next_i].get(next_j, '.')
            while spot != 'L':
                if spot == '#':
                    occupied_seats += 1
                    break
                next_i += delta_i
                next_j += delta_j
                if next_i >= number_of_rows or next_i < 0:
                    break
                spot = seat_map[next_i].get(next_j, 'L')
    return occupied_seats


print(f'Answer 2: {load_passengers(occupied_surrounds_v2, 5, report=False)}')

# PS.: To do this I wanted to see the changes to check it out whether it works or not, as the specification,
# thats why there is the report parameter. If you are interested to see it running:

first_sample = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

lines = first_sample.splitlines()
number_of_rows = len(lines)
number_of_cols = len(lines[0])

print(f'Printing: {load_passengers(occupied_surrounds_v1, report=True)}')
