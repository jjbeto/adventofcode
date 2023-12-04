from aocd import get_data

raw = get_data(day=4, year=2021)

lines = list([n for n in raw.splitlines()])

execution = [int(n) for n in lines[0].split(',')]
boards = []

board = []
for i in range(1, len(lines)):
    if lines[i] == '':
        if board:
            boards.append(board)
        board = []
        continue
    board.append([int(n) for n in lines[i].split(' ') if n])
boards.append(board)  # last board

boards_cols = []
for board in boards:
    v_board = []
    for line in board:
        for col in range(5):
            if len(v_board) == col:
                v_board.append([])
            v_board[col].append(line[col])
    boards_cols.append(v_board)

# each board consists of a group af all its cols and lines
[[boards[i].append(column) for column in board_col] for i, board_col in enumerate(boards_cols)]


def calc(board, grant_last, grant_list):
    return grant_last * sum(set(x for x in [s for sublist in board for s in sublist] if x not in grant_list))


def part1():
    granted = []
    for e in execution:
        granted.append(e)
        for _board in boards:
            for row_or_col in _board:
                if set(row_or_col).issubset(granted):
                    return calc(_board, e, granted)


print(f'Answer 1: {part1()}')


def part2():
    granted, winners, n_boards = set(), set(), len(boards)
    for e in execution:
        granted.add(e)
        for i, board in enumerate(boards):
            if i in winners:
                continue
            for row_or_col in board:
                if all(elem in granted for elem in row_or_col):
                    winners.add(i)
                    if len(winners) == n_boards:
                        return calc(board, e, granted)
    return None


print(f'Answer 2: {part2()}')
