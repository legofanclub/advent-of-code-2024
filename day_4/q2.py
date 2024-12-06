from collections import defaultdict
f = open("input.txt", "r")

grid = []
for line in f:
    grid.append(list(line.strip()))

# do a dfs on each M in the specified direction
target = "MAS"
def dfs(i, j, rsf, direction):
    if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
        # out of bounds
        return None
    elif len(rsf) >= 4:
        # failed to make the word
        return None
    elif rsf + grid[i][j] == target:
        return (i - direction[0], j - direction[1])
    elif grid[i][j] == target[len(rsf)]:
        # correct letter
        return dfs(i + direction[0], j + direction[1], rsf + grid[i][j], direction)
    else:
        return None

directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
centers = defaultdict(int)
for i, row in enumerate(grid):
    for j, element in enumerate(row):
        if element == "M":
            for direction in directions:
                cur_center = dfs(i, j, "", direction)
                if cur_center:
                    centers[cur_center] += 1
                    
print(len([x for x in centers.values() if x > 1]))