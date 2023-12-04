from aocd import get_data

raw = get_data(day=5, year=2020)
lines = raw.splitlines()


def calculate(ticket, pos: range):
    for each in ticket:
        half = int((pos.stop + 1 - pos.start) / 2)
        pos = range(pos.start, pos.stop - half) if each in ['F', 'L'] else range(pos.start + half, pos.stop)
    return pos.stop


def seat_id(ticket):
    row = calculate(ticket[:7], range(127))
    col = calculate(ticket[7:], range(7))
    return row * 8 + col


def highest_seat_id(tickets):
    highest_row = sorted(set([ticket[:7] for ticket in tickets]))[0]
    highest_row_col = sorted([ticket for ticket in tickets if ticket.startswith(highest_row)], reverse=True)[0]
    return seat_id(highest_row_col)


print(f'Answer 1: {highest_seat_id(lines)}')


# Then... I was talking to some colleagues, and they actually had a way better approach to calculate `seat id`!


def seat_id_v2(ticket):
    translation = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
    return int(''.join([translation[letter] for letter in ticket]), 2)


print(f'improving: {seat_id_v2("FBFBBFFRLR")}')


def my_seat(tickets):
    previous = None
    for seat in sorted([seat_id(ticket) for ticket in tickets]):
        current = seat
        if not previous:
            previous = current
        if current - 2 == previous:
            return current - 1
        previous = current
    return -1


print(f'Answer 2: {my_seat(lines)}')


# Then again 😂.. There is a [magical](https://www.quora.com/What-is-the-summation-of-consecutive-numbers-not
# -starting-from-one) way to calculate it in linear way 🚀:

def my_seat_v2(tickets):
    seats = ([seat_id(ticket) for ticket in tickets])
    m, n = min(seats), max(seats)
    return (m + n) * (n - m + 1) / 2 - sum(seats)


print(f'Answe 2 v2: {my_seat_v2(lines)}')
