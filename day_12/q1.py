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
    return total


def all_potential_adjoining(i, j):
    return [(i + a, j + b) for a, b in directions]


def adjoining_tiles(i, j):
    return [(a, b) for a, b in all_potential_adjoining(i, j) if inbounds(a, b)]


def cost_of_fence(i, j, seen):
    if (i, j) in seen:
        return (0, 0)
    seen.add((i, j))

    total_area = 1
    total_perimeter = get_perimeter(i, j)
    plant_letter = puzzle[i][j]

    adjoining_matching_tiles = [
        (a, b) for a, b in adjoining_tiles(i, j) if plant_letter == puzzle[a][b]
    ]

    for a, b in adjoining_matching_tiles:
        area, perimeter = cost_of_fence(a, b, seen)
        total_area += area
        total_perimeter += perimeter

    return (total_area, total_perimeter)


def get_solution() -> int:
    seen = set()

    total_cost = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if (i, j) in seen:
                continue
            area, perimeter = cost_of_fence(i, j, seen)
            total_cost += area * perimeter
    return total_cost


print(get_solution())
