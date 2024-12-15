def get_warehouse_and_moves():
    f = open("input.txt", "r")

    warehouse = []
    for line in f:
        if line == "\n":
            break
        warehouse.append(list(line.strip()))

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
            if val == "O":
                score += 100 * i + j
    return score


def get_robot_position(warehouse):
    for i, row in enumerate(warehouse):
        for j, val in enumerate(row):
            if val == "@":
                return (i, j)


def add_tuples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def execute_move(move, warehouse):
    move_to_direction = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    direction = move_to_direction[move]
    robot_position = get_robot_position(warehouse)

    first_step = cur_pos = add_tuples(robot_position, direction)
    while warehouse[cur_pos[0]][cur_pos[1]] == "O":
        cur_pos = add_tuples(cur_pos, direction)

    if warehouse[cur_pos[0]][cur_pos[1]] == "#":
        return warehouse
    elif warehouse[cur_pos[0]][cur_pos[1]] == ".":
        # if there were no blocks in the way, this is a no-op
        warehouse[cur_pos[0]][cur_pos[1]], warehouse[first_step[0]][first_step[1]] = (
            warehouse[first_step[0]][first_step[1]],
            warehouse[cur_pos[0]][cur_pos[1]],
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
        warehouse = execute_move(move, warehouse)
    return score_result(warehouse)


if __name__ == "__main__":
    print(solve())
