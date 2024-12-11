f = open("input.txt", "r")

puzzle = []

for line in f:
    puzzle.append([int(x) for x in list(line.strip())])

def count_paths(i: int, j: int, count: int, result_set):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # out of bounds
    if not (0 <= i < len(puzzle) and 0 <= j < len(puzzle[0])):
        return

    val = puzzle[i][j]
    
    # invalid path
    if val != count:
        return
    
    # solution
    if val == 9 and count == 9:
        result_set.add((i,j))
        return

    # recursive case
    for a, b in directions:
        count_paths(i+a, j+b, count + 1, cur_result_set)

result = 0
for i, line in enumerate(puzzle):
    for j, val in enumerate(line):
        if val == 0:
            cur_result_set = set()
            count_paths(i, j, 0, cur_result_set)
            num_trails = len(cur_result_set)
            result += num_trails

print(result)