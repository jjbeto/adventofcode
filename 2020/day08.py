from aocd import get_data

raw = get_data(day=8, year=2020)

lines = raw.splitlines()


def fix_loop_v1():
    index = 0
    visited = []
    accumulator = 0
    for _ in range(len(lines)):
        if index in visited:
            break

        instruction = lines[index].split(' ')
        visited.append(index)

        accumulator += int(instruction[1]) if instruction[0] == 'acc' else 0
        index += int(instruction[1]) if instruction[0] == 'jmp' else 1
    return accumulator


print(f'Answer 1: {fix_loop_v1()}')


def fix_loop_v2():
    index = 0
    switch = []
    accumulator = 0
    while index < len(lines):
        index = 0
        visited = []
        accumulator = 0
        switched = False
        for _ in range(len(lines)):
            if index >= len(lines) or index in visited:
                break
            instruction = lines[index].split(' ')
            visited.append(index)
            accumulator += int(instruction[1]) if instruction[0] == 'acc' else 0
            if instruction[0] != 'acc' and index not in switch and not switched:
                print(f'switch [{"jmp->nop" if instruction[0] == "jmp" else "nop->jmp"}] at {index}')
                instruction[0] = 'nop' if instruction[0] == 'jmp' else 'jmp'
                switch.append(index)
                switched = True
            index += int(instruction[1]) if instruction[0] == 'jmp' else 1
    return accumulator


print(f'Answer 2: {fix_loop_v2()}')
