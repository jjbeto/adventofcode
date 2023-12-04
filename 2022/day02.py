from aocd import get_data

raw = get_data(day=2, year=2022)

# outcome (0=lost, 3=draw, 6=won) + shape (1=rock, 2=paper, 3=scissors)
score = 0  # result() + shape
for line in raw.splitlines():
    if line == 'A X':  # rock x rock = draw
        score += 3 + 1
    elif line == 'A Y':  # rock x paper = won
        score += 6 + 2
    elif line == 'A Z':  # rock x scissors = lost
        score += 0 + 3
    elif line == 'B X':  # paper x rock = lost
        score += 0 + 1
    elif line == 'B Y':  # paper x paper = draw
        score += 3 + 2
    elif line == 'B Z':  # paper x scissors = won
        score += 6 + 3
    elif line == 'C X':  # scissors x rock = won
        score += 6 + 1
    elif line == 'C Y':  # scissors x paper = lost
        score += 0 + 2
    elif line == 'C Z':  # scissors x scissors = draw
        score += 3 + 3

print(f'Answer 1: {score}')

# outcome (0=lost, 3=draw, 6=won) + shape (1=rock, 2=paper, 3=scissors)
# needed outcome: X=lose, Y=draw, Z=win
score = 0  # result() + shape
for line in raw.splitlines():
    if line == 'A X':  # rock x scissors = lost
        score += 0 + 3
    elif line == 'A Y':  # rock x rock = draw
        score += 3 + 1
    elif line == 'A Z':  # rock x paper = won
        score += 6 + 2
    elif line == 'B X':  # paper x rock = lost
        score += 0 + 1
    elif line == 'B Y':  # paper x paper = draw
        score += 3 + 2
    elif line == 'B Z':  # paper x scissors = won
        score += 6 + 3
    elif line == 'C X':  # scissors x paper = lost
        score += 0 + 2
    elif line == 'C Y':  # scissors x scissors = draw
        score += 3 + 3
    elif line == 'C Z':  # scissors x rock = won
        score += 6 + 1

print(f'Answer 2: {score}')
