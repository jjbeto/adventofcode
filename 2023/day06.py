def solve(matches):
    total = 1
    for m in matches:
        amount = 0
        for t in range(m[0]):
            val = t * (m[0] - t)
            if val < m[1] and amount > 0:
                break
            if val > m[1]:
                amount += 1
        total *= amount
    return total


print(f'Answer 1: {solve([(7, 9), (15, 40), (30, 200)])}')
print(f'Answer 2: {solve([(71530, 940200)])}')
