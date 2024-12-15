def double_warehouse_line(wl):
    result = []
    for c in wl:
        if c == "#":
            result += ["#", "#"]
        elif c == ".":
            result += [".", "."]
        elif c == "@":
            result += ["@", "."]
        elif c == "O":
            result += ["[", "]"]
    return result


def get_warehouse_and_moves():
    f = open("input.txt", "r")

    warehouse = []
    for line in f:
        if line == "\n":
            break
        warehouse.append(double_warehouse_line(list(line.strip())))

    moves = []
    for line in f:
        moves += list(line.strip())

    return warehouse, moves


def print_warehouse(warehouse):
    for line in warehouse:
        print("".join(line))


def score_result(warehouse):
    score = 0
    for i, row in enumerate(warehouse):
        for j, val in enumerate(row):
            if val == "[":
                score += 100 * i + j
    return score


def get_robot_position(warehouse):
    for i, row in enumerate(warehouse):
        for j, val in enumerate(row):
            if val == "@":
                return (i, j)


def add_tuples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def execute_ud_move(move, warehouse):
    assert move in ["^", "v"]
    move_to_direction = {"^": (-1, 0), "v": (1, 0)}
    robot_position = get_robot_position(warehouse)

    next_position = add_tuples(robot_position, move_to_direction[move])

    thing_in_way = warehouse[next_position[0]][next_position[1]]
    if thing_in_way == "#":
        return warehouse
    elif thing_in_way == ".":
        (
            warehouse[next_position[0]][next_position[1]],
            warehouse[robot_position[0]][robot_position[1]],
        ) = (
            warehouse[robot_position[0]][robot_position[1]],
            warehouse[next_position[0]][next_position[1]],
        )
        return warehouse

    # now we're only left with the case where there's a box in our way
    if move == "^":
        all_boxes_to_move = get_all_pushes_above(
            next_position[0], next_position[1], warehouse, set()
        )
        if can_move_all_boxes_up(all_boxes_to_move, warehouse):
            warehouse = move_boxes_up(all_boxes_to_move, warehouse)

            # move robot
            (
                warehouse[next_position[0]][next_position[1]],
                warehouse[robot_position[0]][robot_position[1]],
            ) = (
                warehouse[robot_position[0]][robot_position[1]],
                warehouse[next_position[0]][next_position[1]],
            )

    elif move == "v":
        all_boxes_to_move = get_all_pushes_below(
            next_position[0], next_position[1], warehouse, set()
        )
        if can_move_all_boxes_down(all_boxes_to_move, warehouse):
            warehouse = move_boxes_down(all_boxes_to_move, warehouse)

            # move robot
            (
                warehouse[next_position[0]][next_position[1]],
                warehouse[robot_position[0]][robot_position[1]],
            ) = (
                warehouse[robot_position[0]][robot_position[1]],
                warehouse[next_position[0]][next_position[1]],
            )

    return warehouse


def move_boxes_up(all_boxes_to_move, warehouse):
    boxes = list(all_boxes_to_move)
    boxes.sort(key=lambda x: x[0])

    # move boxes going from top to bottom
    for i, j in boxes:
        warehouse[i][j], warehouse[i - 1][j] = ".", warehouse[i][j]

    return warehouse


def move_boxes_down(all_boxes_to_move, warehouse):
    boxes = list(all_boxes_to_move)
    boxes.sort(key=lambda x: x[0], reverse=True)

    # move boxes going from bottom to top
    for i, j in boxes:
        warehouse[i][j], warehouse[i + 1][j] = ".", warehouse[i][j]

    return warehouse


def can_move_all_boxes_up(all_boxes, warehouse):
    for i, j in all_boxes:
        if warehouse[i - 1][j] == "#":
            return False
    return True


def can_move_all_boxes_down(all_boxes, warehouse):
    for i, j in all_boxes:
        if warehouse[i + 1][j] == "#":
            return False
    return True


def get_all_pushes_above(i, j, warehouse, seen):
    """returns the set of all box parts that will be pushed upwards by pushing the initial box part up"""
    if (i, j) in seen:
        return set()
    else:
        seen.add((i, j))

    apu = set([(i, j)])
    if warehouse[i][j] == "[":
        return (
            apu
            | get_all_pushes_above(i, j + 1, warehouse, seen)
            | get_all_pushes_above(i - 1, j, warehouse, seen)
        )
    elif warehouse[i][j] == "]":
        return (
            apu
            | get_all_pushes_above(i, j - 1, warehouse, seen)
            | get_all_pushes_above(i - 1, j, warehouse, seen)
        )
    else:
        return set()


def get_all_pushes_below(i, j, warehouse, seen):
    """returns the set of all box parts that will be pushed downwards by pushing the initial box part down"""
    if (i, j) in seen:
        return set()
    else:
        seen.add((i, j))

    apu = set([(i, j)])
    if warehouse[i][j] == "[":
        return (
            apu
            | get_all_pushes_below(i, j + 1, warehouse, seen)
            | get_all_pushes_below(i + 1, j, warehouse, seen)
        )
    elif warehouse[i][j] == "]":
        return (
            apu
            | get_all_pushes_below(i, j - 1, warehouse, seen)
            | get_all_pushes_below(i + 1, j, warehouse, seen)
        )
    else:
        return set()


def execute_lr_move(move, warehouse):
    # left and right moves work largely like in Q1
    assert move in ["<", ">"]

    move_to_direction = {"<": (0, -1), ">": (0, 1)}
    direction = move_to_direction[move]
    robot_position = get_robot_position(warehouse)

    first_step = cur_pos = add_tuples(robot_position, direction)
    while warehouse[cur_pos[0]][cur_pos[1]] in ["[", "]"]:
        cur_pos = add_tuples(cur_pos, direction)

    if warehouse[cur_pos[0]][cur_pos[1]] == "#":
        return warehouse
    elif warehouse[cur_pos[0]][cur_pos[1]] == ".":
        # have to move all the parentheses one over
        if move == "<":
            for a in range(cur_pos[1], first_step[1]):
                warehouse[cur_pos[0]][a], warehouse[cur_pos[0]][a + 1] = (
                    warehouse[cur_pos[0]][a + 1],
                    warehouse[cur_pos[0]][a],
                )
        elif move == ">":
            for a in range(cur_pos[1], first_step[1], -1):
                warehouse[cur_pos[0]][a], warehouse[cur_pos[0]][a - 1] = (
                    warehouse[cur_pos[0]][a - 1],
                    warehouse[cur_pos[0]][a],
                )

    # move the robot to the now empty first step position
    (
        warehouse[first_step[0]][first_step[1]],
        warehouse[robot_position[0]][robot_position[1]],
    ) = (
        warehouse[robot_position[0]][robot_position[1]],
        warehouse[first_step[0]][first_step[1]],
    )
    return warehouse


def solve():
    warehouse, moves = get_warehouse_and_moves()
    for move in moves:
        if move in ["<", ">"]:
            warehouse = execute_lr_move(move, warehouse)
        else:
            warehouse = execute_ud_move(move, warehouse)
    return score_result(warehouse)


if __name__ == "__main__":
    print(solve())
