from collections import defaultdict
from functools import cache


def get_puzzle():
    f = open("input.txt", "r")
    puzzle = []
    for line in f:
        puzzle.append(line.strip())
    return puzzle


def tuple_add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


@cache
def get_target_location(target, numeric):
    if numeric:
        grid = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["x", "0", "A"]]
    else:
        grid = [["x", "^", "A"], ["<", "v", ">"]]

    for i, line in enumerate(grid):
        for j, val in enumerate(line):
            if val == target:
                return (i, j)


@cache
def get_path_for_code(code, initial_position, numeric):
    """
    takes a code in the form <<^^A and returns the code that's needed in the next level: eg. ^^^>>A
    """

    # memoizing this function gives a >10x speedup
    if numeric:
        grid = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["x", "0", "A"]]
    else:
        grid = [["x", "^", "A"], ["<", "v", ">"]]

    if code == "":
        return [], initial_position

    target = code[0]

    # find target location
    target_location = get_target_location(target, numeric)

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

    if x_thing == None or y_thing == None:
        path_from_init_to_target = r1
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
            # r1 has x_thing first
            # r2 has y_thing first

            # the order of movement doesn't matter for the 1st or the 2nd level, but for the 3rd level, if we do the harder moves first (on the first level), it is faster
            cost = {"^": 2, ">": 2, "v": 4, "<": 6, "A": 0}

            if cost[x_thing] > cost[y_thing]:
                path_from_init_to_target = r1
            else:
                path_from_init_to_target = r2

        elif not r1_bad:
            path_from_init_to_target = r1
        elif not r2_bad:
            path_from_init_to_target = r2
        else:
            raise AssertionError("this shouldn't happen")

    final_path, final_location = get_path_for_code(code[1:], target_location, numeric)
    return path_from_init_to_target + final_path, final_location


def get_path_for_directional_input(code):
    result = defaultdict(int)
    location = (0, 2)
    for (p, l), val in code.items():
        sub_paths = [x + "A" for x in "".join(p).split("A")][:-1]
        location = l
        for sp in sub_paths:
            path, end_location = get_path_for_code(sp, location, False)
            result[(tuple(path), location)] += val
            location = end_location

    return result


def solve():
    puzzle = get_puzzle()
    result = 0

    for code in puzzle:
        path_for_numeric, _ = get_path_for_code(
            code,
            (3, 2),
            True,
        )

        code_for_kp_n_minus_1 = {(tuple(path_for_numeric), (0, 2)): 1}

        for i in range(25):
            codes_for_kp_n = get_path_for_directional_input(code_for_kp_n_minus_1)
            code_for_kp_n_minus_1 = codes_for_kp_n

        shortest_path = codes_for_kp_n
        shortest_path_len = sum([len(k[0]) * v for k, v in shortest_path.items()])

        numeric_part = int("".join([x for x in code if x.isnumeric()]))
        result += shortest_path_len * numeric_part

    return result


print(solve())
