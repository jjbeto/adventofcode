from aocd import get_data

raw = get_data(day=15, year=2020)


def game(numbers, position):
    memory = {n: i + 1 for i, n in enumerate(numbers)}
    spoken = numbers[-1]
    turn = len(numbers)

    while turn < position:
        previous = memory.get(spoken)
        memory[spoken] = turn
        spoken = turn - previous if previous else 0
        turn += 1
    return spoken


start_numbers = [13, 16, 0, 12, 15, 1]

print(f"Answer 1: {game(start_numbers, 2020)}")
print(f"Answer 2: {game(start_numbers, 30_000_000)}")
