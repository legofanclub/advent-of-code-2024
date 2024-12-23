def get_puzzle():
    f = open("input.txt", "r")
    puzzle = []
    for line in f:
        puzzle.append(line.strip())
    return puzzle


def tuple_add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def get_all_paths_grid(code, initial_position, grid):
    if code == "":
        return [[]]

    target = code[0]
    result = []

    # find target location
    target_location = (-1, -1)
    for i, line in enumerate(grid):
        for j, val in enumerate(line):
            if val == target:
                target_location = (i, j)

    x_diff = target_location[1] - initial_position[1]
    y_diff = target_location[0] - initial_position[0]

    # append 2 results one with x diff handled first and one with y diff handled first
    if x_diff < 0:
        x_thing = "<"
    elif x_diff > 0:
        x_thing = ">"
    else:
        x_thing = None

    if y_diff < 0:
        y_thing = "^"
    elif y_diff > 0:
        y_thing = "v"
    else:
        y_thing = None

    r1 = [x_thing] * abs(x_diff) + [y_thing] * abs(y_diff) + ["A"]
    r2 = [y_thing] * abs(y_diff) + [x_thing] * abs(x_diff) + ["A"]

    if r1 == r2:
        result = [r1]
    else:
        # handle path going through invalid space
        r1_bad = False
        r2_bad = False

        thing_to_vector = {
            "^": (-1, 0),
            "v": (1, 0),
            "<": (0, -1),
            ">": (0, 1),
            "A": (0, 0),
        }
        cur = initial_position
        for move in r1:
            cur = tuple_add(cur, thing_to_vector[move])
            if grid[cur[0]][cur[1]] == "x":
                r1_bad = True
                break

        cur = initial_position
        for move in r2:
            cur = tuple_add(cur, thing_to_vector[move])
            if grid[cur[0]][cur[1]] == "x":
                r2_bad = True
                break

        if not (r1_bad or r2_bad):
            result = [r1, r2]
        elif not r1_bad:
            result = [r1]
        elif not r2_bad:
            result = [r2]
        else:
            raise AssertionError("this shouldn't happen")

    # combine result to get from current position to 1st letter in code with the result for the next steps
    l = []
    sub_lists = get_all_paths_grid(code[1:], target_location, grid)
    for x in result:
        for y in sub_lists:
            l.append(x + y)

    return l


def get_all_paths_directional_input(list_of_code_lists):
    result = []
    for i, l in enumerate(list_of_code_lists):
        result += get_all_paths_grid(
            "".join(l), (0, 2), [["x", "^", "A"], ["<", "v", ">"]]
        )
    return result


def solve():
    puzzle = get_puzzle()

    result = 0

    for code in puzzle:
        codes_for_kp2 = get_all_paths_grid(
            code,
            (3, 2),
            [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["x", "0", "A"]],
        )
        codes_for_kp3 = get_all_paths_directional_input(codes_for_kp2)
        codes_for_text_input = get_all_paths_directional_input(codes_for_kp3)

        shortest_path = min(codes_for_text_input, key=len)
        shortest_path_len = len(shortest_path)
        numeric_part = int("".join([x for x in code if x.isnumeric()]))

        result += shortest_path_len * numeric_part
    return result


print(solve())
