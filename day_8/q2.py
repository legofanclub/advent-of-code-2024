from itertools import combinations

f = open("input.txt", "r")
puzzle_input = []
for line in f:
    puzzle_input.append(list(line.strip()))

uniques = set()
for line in puzzle_input:
    for val in line:
        uniques.add(val)
uniques.remove(".") # '.' is not an antenna

def inbounds(point):
    return 0 <= point[0] < len(puzzle_input) and 0 <= point[1] < len(puzzle_input[0])

def count_antinodes_in_pair(a, b):
    y1, x1 = a
    y2, x2 = b

    x_diff = x1 - x2
    y_diff = y1 - y2

    result = []

    for i in range(-100, 100):
        p1 = (y1 - i*(2 * y_diff), x1 - i*(2 * x_diff))
        p2 = (y2 + i*(2 * y_diff), x2 + i*(2 * x_diff))

        if inbounds(p1):
            result.append(p1)
        if inbounds(p2):
            result.append(p2)
    
    return result

def get_antinodes(coords):
    result = set()
    for a, b in combinations(coords, 2):
        result.update(count_antinodes_in_pair(a, b))
    return result

antinodes = set()
for c in list(uniques):
    coords = []
    for i, line in enumerate(puzzle_input):
        for j, val in enumerate(line):
            if val == c:
                coords.append((i,j))
    
    ant = get_antinodes(coords)
    antinodes.update(ant)

print(len(antinodes))