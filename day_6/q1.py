f = open("input.txt", "r")

puzzle_map = []
for line in f:
    puzzle_map.append(list(line.strip()))

def print_map(m):
    for line in m:
        print("".join(line))

char_to_direction = {"^" : (-1, 0), ">" : (0, 1), "<" : (0, -1), "v" : (1, 0)}

direction = (0, 0) # fake direction to start with
position = (0, 0) # fake position to start with
for i, line in enumerate(puzzle_map):
    for j, val in enumerate(line):
        if val in char_to_direction.keys():
            position = (i, j)
            direction = char_to_direction[val]

def position_inbounds(position):
    return 0 <= position[0] < len(puzzle_map[0]) and 0 <= position[1] < len(puzzle_map[1])

def tuple_add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

seen = set()
while position_inbounds(position):

    if (position, direction) in seen:
        break
    seen.add((position, direction))

    next_position = tuple_add(position, direction)

    while position_inbounds(next_position):
        obj_in_path = puzzle_map[next_position[0]][next_position[1]]
        if obj_in_path == '#':
            direction = (direction[1], -direction[0])
            next_position = tuple_add(position, direction)
            continue
        break
    puzzle_map[position[0]][position[1]] = "X"
     
    position = next_position

result = 0
for line in puzzle_map:
    for val in line:
        if val == "X":
            result += 1

print(result)
