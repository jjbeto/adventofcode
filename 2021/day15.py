from queue import PriorityQueue

from aocd import get_data

raw = get_data(day=15, year=2021)
data = [n for n in raw.splitlines()]


def part1(lines):
    risks = [list(map(int, line.strip())) for line in lines]
    paths = [[float('inf')] * len(line) for line in lines]
    paths[0][0] = 0
    square_size = len(paths)

    queue = PriorityQueue()
    queue.put((0, 0, 0))  # risk, x, y
    while not queue.empty():
        total, x, y = queue.get()
        for edge_x, edge_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= edge_x < square_size and 0 <= edge_y < square_size:
                edge_value = total + risks[edge_y][edge_x]
                if edge_value < paths[edge_y][edge_x]:
                    paths[edge_y][edge_x] = edge_value
                    queue.put((edge_value, edge_x, edge_y))
    return paths[len(paths) - 1][len(paths[0]) - 1]


print(f'Answer 1: {part1(data)}')


def part2(lines):
    def rotate(text):
        return ''.join(f'{int(t) + 1}' if int(t) < 9 else '1' for t in text)

    big_picture = lines.copy()
    tile = lines.copy()
    for _ in range(4):
        for i, line in enumerate(tile):
            tile[i] = rotate(line)
            big_picture[i] += tile[i]

    shadow_picture = big_picture.copy()
    for _ in range(4):
        for i, line in enumerate(shadow_picture):
            shadow_picture[i] = rotate(line)
            big_picture.append(shadow_picture[i])

    return part1(big_picture)


print(f'Answer 2: {part2(data)}')
