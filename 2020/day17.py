from aocd import get_data

raw = get_data(day=17, year=2020)


def find_neighbors(coordinate):
    if len(coordinate) == 3:
        neighbors = set([(coordinate[0] + _x, coordinate[1] + _y, coordinate[2] + _z)
                         for _x in [-1, 0, +1]
                         for _y in [-1, 0, +1]
                         for _z in [-1, 0, +1]])
    else:
        neighbors = set([(coordinate[0] + _x, coordinate[1] + _y, coordinate[2] + _z, coordinate[3] + _w)
                         for _x in [-1, 0, +1]
                         for _y in [-1, 0, +1]
                         for _z in [-1, 0, +1]
                         for _w in [-1, 0, +1]])
    neighbors.remove(coordinate)
    return neighbors


def run(coordinates):
    for _ in range(6):
        active = set()
        neighbors = set()
        for coordinate in coordinates:
            _neighbors = find_neighbors(coordinate)
            neighbors.update(_neighbors)
            if 2 <= len(_neighbors.intersection(coordinates)) <= 3:
                active.add(coordinate)
        for coordinate in neighbors - coordinates:
            if len(find_neighbors(coordinate).intersection(coordinates)) == 3:
                active.add(coordinate)

        coordinates = active
    return len(coordinates)


data = '''####.#..
.......#
#..#####
.....##.
##...###
#..#.#.#
.##...#.
#...##..'''

coordinates_3d = set((x, y, 0)
                     for y, line in enumerate(data.splitlines())
                     for x, value in enumerate(line) if value == '#')
print(f"Answer 1: {run(coordinates_3d)}")

coordinates_4d = set((x, y, 0, 0)
                     for y, line in enumerate(data.splitlines())
                     for x, value in enumerate(line) if value == '#')
print(f"Answer 2: {run(coordinates_4d)}")
