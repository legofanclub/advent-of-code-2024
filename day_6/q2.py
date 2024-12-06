# took 25.50s to run placing blocks everywhere
# took 4.43s to run after only placing blocks in the guard's original path

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

start_position = position
initial_direction = direction

def position_inbounds(position):
    return 0 <= position[0] < len(puzzle_map[0]) and 0 <= position[1] < len(puzzle_map[1])

def tuple_add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def did_loop(puzzle_map, start_position, initial_direction) -> bool:
    position = start_position
    direction = initial_direction
    
    seen = set()
    while position_inbounds(position):

        if (position, direction) in seen:
            return True
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
    
    return False

def getQ1Answer(puzzle_map, start_position, initial_direction):
    position = start_position
    direction = initial_direction
    
    seen = set()
    while position_inbounds(position):

        if (position, direction) in seen:
            return True
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
    
    return puzzle_map

q1Answer = getQ1Answer([x.copy() for x in puzzle_map], start_position, initial_direction)
result = 0
for i in range(len(puzzle_map)):
    for j in range(len(puzzle_map[0])):
        if (i, j) != start_position and q1Answer[i][j] == 'X':
            original = puzzle_map[i][j]
            puzzle_map[i][j] = "#"
            if did_loop([x.copy() for x in puzzle_map], start_position, initial_direction):
                result += 1
            puzzle_map[i][j] = original # set the map back to what it was

print(result)
