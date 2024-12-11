f = open("input.txt", "r")

puzzle = []

for line in f:
    puzzle.append([int(x) for x in list(line.strip())])

def count_paths(i: int, j: int, count: int):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # out of bounds
    if not (0 <= i < len(puzzle) and 0 <= j < len(puzzle[0])):
        return 0

    val = puzzle[i][j]
    
    # invalid path
    if val != count:
        return 0
    
    # solution
    if val == 9 and count == 9:
        return 1

    num_paths = 0
    # recursive case
    for a, b in directions:
        num_paths += count_paths(i+a, j+b, count + 1)
    return num_paths

result = 0
for i, line in enumerate(puzzle):
    for j, val in enumerate(line):
        if val == 0:
            num_trails = count_paths(i, j, 0,)
            result += num_trails

print(result)