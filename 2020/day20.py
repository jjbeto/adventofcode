import math

test = '''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...'''


def load_all_borders(tile):
    borders = [
        tile[1],
        tile[-1],
        ''.join([line[0] for line in tile[1:]]),
        ''.join([line[-1] for line in tile[1:]])
    ]
    return borders + [_b[::-1] for _b in borders]  # borders + reverted borders (doubled)


text = test
# text = open('day20.data').read()
borders = {}
for each in text.split('\n\n'):
    tile = each.split('\n')
    _id = tile[0][:-1].split(' ')[1]
    borders[_id] = load_all_borders(tile)

# intersections = {}
# for id_compared in borders:
#     intersections[id_compared] = sum(
#         [
#             len([border_compared
#                  for border_check in borders[id_check]
#                  for border_compared in borders[id_compared] if border_compared == border_check])
#             for id_check in borders if id_check != id_compared
#         ]
#     ) // 2  # remove duplications

intersections = {}
for id_compared in borders:
    intersections[id_compared] = [{id_check
                                   for border_check in borders[id_check]
                                   for border_compared in borders[id_compared] if border_compared == border_check}
                                  for id_check in borders if id_check != id_compared]
    intersections[id_compared] = [_id
                                  for id_group in intersections[id_compared]
                                  for _id in id_group]

corners = [int(_id) for _id in borders if len(intersections[_id]) == 2]
print(corners)
print(math.prod(corners))

####################### p2

images = {}
for each in text.split('\n\n'):
    tile = each.split('\n')
    _id = tile[0][:-1].split(' ')[1]
    images[_id] = [t[1:-1] for t in tile[2:-1]]


# '2311' = ['1951', '1427', '3079']
# '1951' = ['2311', '2729']
# '1171' = ['1489', '2473']
# '1427' = ['2311', '1489', '2473', '2729']
# '1489' = ['1171', '1427', '2971']
# '2473' = ['1171', '1427', '3079']
# '2971' = ['1489', '2729']
# '2729' = ['1951', '1427', '2971']
# '3079' = ['2311', '2473']

def load_row(start):
    deep = math.sqrt(len(intersections))

    i = 0
    neighbors = intersections[start]
    row = []
    while i < deep:
        next_neighbor = neighbors[i]
