from collections import deque


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


def solve():
    puzzle, start, end = get_puzzle()
    shortest_path = get_shortest_path(puzzle, start, end)

    for i, (y, x) in enumerate(shortest_path):
        puzzle[y][x] = i

    required_speedup = 100
    result = 0
    for i, line in enumerate(puzzle):
        for j, val in enumerate(line):
            if str(val).isnumeric():
                location = (i, j)
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for direction in directions:
                    new_location = tuple_add(location, direction)
                    if (
                        inbounds(new_location, puzzle)
                        and not str(
                            puzzle[new_location[0]][new_location[1]]
                        ).isnumeric()
                    ):
                        second_hop = tuple_add(new_location, direction)
                        if (
                            inbounds(second_hop, puzzle)
                            and str(puzzle[second_hop[0]][second_hop[1]]).isnumeric()
                        ):
                            val2 = puzzle[second_hop[0]][second_hop[1]]
                            if val2 > val and (val2 - val - 1) >= required_speedup:
                                result += 1
    return result


print(solve())
