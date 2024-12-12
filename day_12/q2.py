f = open("input.txt", "r")
puzzle = []
for line in f:
    puzzle.append(list(line.strip()))

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def inbounds(i: int, j: int) -> int:
    width = len(puzzle[0])
    height = len(puzzle)
    return 0 <= i < height and 0 <= j < width


def get_perimeter(i: int, j: int) -> int:
    cur_val = puzzle[i][j]
    total = 0
    for a, b in all_potential_adjoining(i, j):
        if not inbounds(a, b) or puzzle[a][b] != cur_val:
            total += 1
    if total == 4:
        return 0
    elif total == 3:
        return 1
    elif total == 2:
        return
    return total


def all_potential_adjoining(i, j):
    return [(i + a, j + b) for a, b in directions]


def adjoining_tiles(i, j):
    return [(a, b) for a, b in all_potential_adjoining(i, j) if inbounds(a, b)]


def cost_of_fence(i, j, seen):
    if (i, j) in seen:
        return (0, set())
    seen.add((i, j))

    total_area = 1
    all_squares = set([(i, j)])
    plant_letter = puzzle[i][j]

    adjoining_matching_tiles = [
        (a, b) for a, b in adjoining_tiles(i, j) if plant_letter == puzzle[a][b]
    ]

    for a, b in adjoining_matching_tiles:
        area, squares = cost_of_fence(a, b, seen)
        total_area += area
        all_squares = all_squares.union(squares)

    return (total_area, all_squares)


def num_sides(s) -> int:
    edges = set()
    num_sides = 0

    # have to sort to avoid double counting edges
    s = list(s)
    s.sort(key=lambda x: x[0])
    s.sort(key=lambda x: x[1])

    for i, j in s:
        adjoining_gaps = set(all_potential_adjoining(i, j)) - set(s)
        for a, b in adjoining_gaps:
            edge = (i + (a - i) * 0.5, j + (b - j) * 0.5)
            directionality = (a - i) > 0 or (b - j) > 0
            edges.add((directionality, edge))
            if (
                (directionality, (edge[0] + 1, edge[1])) in edges
                or (directionality, (edge[0] - 1, edge[1])) in edges
            ) and edge[0] // 1 == edge[0]:
                pass
            elif (
                (directionality, (edge[0], edge[1] + 1)) in edges
                or (directionality, (edge[0], edge[1] - 1)) in edges
            ) and edge[1] // 1 == edge[1]:
                pass
            else:
                num_sides += 1
    return num_sides


def get_solution() -> int:
    seen = set()
    total_cost = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if (i, j) in seen:
                continue
            area, squares = cost_of_fence(i, j, seen)
            sides = num_sides(squares)
            total_cost += area * sides
    return total_cost


print(get_solution())
