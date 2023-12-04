from collections import defaultdict

from aocd import get_data

raw = get_data(day=12, year=2021)
data = [n for n in raw.splitlines()]


def part1(lines):
    graph = defaultdict(list)

    for each in lines:
        a_b = each.split('-')
        graph[a_b[0]].append(a_b[1])
        graph[a_b[1]].append(a_b[0])

    def find_path(origin, dest, path, paths):
        path.append(origin)
        if origin == dest:
            paths.append(path.copy())
        else:
            for edge in [e for e in graph[origin] if e.isupper() or e not in path + ['start']]:
                paths = find_path(edge, dest, path, paths)
        path.pop()
        return paths

    return len(find_path('start', 'end', [], []))


print(f'Answer 1: {part1(data)}')


def part2(lines):
    graph = defaultdict(list)

    for each in lines:
        a_b = each.split('-')
        graph[a_b[0]].append(a_b[1])
        graph[a_b[1]].append(a_b[0])

    def find_path(origin, dest, path, paths, memory):
        path.append(origin)
        memory[origin] += 0 if origin.isupper() else 1
        if origin == dest:
            paths.append(path.copy())
        else:
            for edge in graph[origin]:
                if edge == 'start' or max(memory.values()) == 2 and memory[edge] >= 1:
                    continue
                paths, memory = find_path(edge, dest, path, paths, memory)
        memory[path.pop()] -= 1
        return paths, memory

    possibilities, _ = find_path('start', 'end', [], [], defaultdict(int))
    return len(possibilities)


print(f'Answer 2: {part2(data)}')
