f = open("input.txt", "r")

grid = []
for line in f:
    grid.append(list(line.strip()))

# do a dfs on each X in the specified direction
target = "XMAS"
def dfs(i, j, rsf, direction):
    if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
        # out of bounds
        return 0
    elif len(rsf) >= 4:
        # failed to make the word
        return 0
    elif rsf + grid[i][j] == target:
        return 1
    elif grid[i][j] == target[len(rsf)]:
        # correct letter
        return dfs(i + direction[0], j + direction[1], rsf + grid[i][j], direction)
    else:
        return 0
    


directions = [(1,0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
result = 0
for i, row in enumerate(grid):
    for j, element in enumerate(row):
        if element == "X":
            for direction in directions:
                cur_words = dfs(i, j, "", direction)
                result += cur_words
print(result)