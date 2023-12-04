from aocd import get_data

raw = get_data(day=3, year=2020)
lines = raw.splitlines()
columns = len(lines[0])


def search(col_delta, row_delta):
    counter = 0
    col = 0
    row = 0
    while row < len(lines):
        if lines[row][col] == '#':
            counter += 1
        row += row_delta
        col = (col + col_delta) % columns
    return counter


print(f'Answer 1: {search(3, 1)}')
print(f'Answer 2: {search(1, 1) * search(3, 1) * search(5, 1) * search(7, 1) * search(1, 2)}')

# An alternative solution to search by [cmears](https://gitlab.com/cmears) 🚀:

trees = [[(col, row) for col, char in enumerate(line) if char == '#'] for row, line in enumerate(lines)]
trees = [item for sublist in trees for item in sublist]


def search_v2(col, row):
    return [((col + index * col) % columns, index + row) for index in range(0, len(lines), row)]


path = search_v2(3, 1)
matches = [t for t in path if t in trees]

print(f'Answer v2: {len(matches)}')
