from collections import deque
from functools import cache
import numbers


def get_puzzle():
    f = open("input.txt", "r")
    puzzle = []
    for line in f:
        puzzle.append(list(line.strip()))

    for i, line in enumerate(puzzle):
        for j, elem in enumerate(line):
            if elem == "S":
                start = (i, j)
            elif elem == "E":
                end = (i, j)

    return puzzle, start, end


def pprint(p):
    for line in p:
        fat_line = []
        for elem in line:
            elem = str(elem)
            diff = 3 - len(elem)
            fat_line.append(" " * diff + elem)
        print("".join(fat_line))


def tuple_add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def inbounds(point, puzzle):
    return 0 <= point[0] < len(puzzle) and 0 <= point[1] < len(puzzle[0])


def get_shortest_path(puzzle, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    counter = 0
    q = deque([(start, counter, [])])

    seen = set()
    while len(q) > 0:
        location, counter, path = q.popleft()

        if location == end:
            path.append(location)
            return path
        elif (
            location in seen
            or not inbounds(location, puzzle)
            or puzzle[location[0]][location[1]] == "#"
        ):
            continue
        seen.add(location)
        path.append(location)

        for direction in directions:
            new_location = tuple_add(direction, location)
            q.append((new_location, counter + 1, path))


def num_cheats(location, puzzle):
    value = puzzle[location[0]][location[1]]
    if not isinstance(value, numbers.Number):
        return 0

    required_speedup = 100
    target = required_speedup + value

    num_cheating_moves = 20

    @cache
    def dfs(location, target, counter):
        if counter > num_cheating_moves or not inbounds(location, puzzle):
            return set()

        result = set()
        value = puzzle[location[0]][location[1]]

        if isinstance(value, numbers.Number) and value - counter + 1 > target:
            result.add(location)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            new_location = tuple_add(location, direction)
            result = result | dfs(new_location, target, counter + 1)

        return result

    return len(dfs(location, target, 0))


def solve():
    puzzle, start, end = get_puzzle()
    shortest_path = get_shortest_path(puzzle, start, end)

    for i, (y, x) in enumerate(shortest_path):
        puzzle[y][x] = i

    result = 0
    for i, line in enumerate(puzzle):
        for j, _ in enumerate(line):
            result += num_cheats((i, j), puzzle)
    return result


print(solve())
