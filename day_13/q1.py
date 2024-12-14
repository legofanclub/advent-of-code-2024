def get_puzzle():
    f = open("input.txt", "r")
    puzzle = []
    cur = {}
    for line in f:
        line = line.strip().split()
        if len(line) == 0:
            puzzle.append(cur)
            cur = {}
        elif line[0] == "Button" and line[1] == "A:":
            x = line[2][2:-1]
            y = line[3][2:]
            cur["a"] = (int(x), int(y))
        elif line[0] == "Button" and line[1] == "B:":
            x = line[2][2:-1]
            y = line[3][2:]
            cur["b"] = (int(x), int(y))
        elif line[0] == "Prize:":
            x = line[1][2:-1]
            y = line[2][2:]
            cur["prize"] = (int(x), int(y))
    # add the last group if there's no trailing linebreak
    if len(cur) > 0:
        puzzle.append(cur)
    return puzzle


def calc_min_cost(elem):
    a_x, a_y = elem["a"]
    b_x, b_y = elem["b"]
    prize_x, prize_y = elem["prize"]

    # button presses are limited to 100 max, so we can try all 10 000 combinations
    min_cost = float("inf")
    for b_presses in range(0, 101):
        for a_presses in range(0, 101):
            if (
                a_x * a_presses + b_x * b_presses == prize_x
                and a_y * a_presses + b_y * b_presses == prize_y
            ):
                min_cost = min(min_cost, a_presses * 3 + b_presses)

    if min_cost == float("inf"):
        # don't press any buttons because we can't get a prize
        min_cost = 0
    return min_cost


def solve_puzzle():
    puzzle = get_puzzle()
    result = 0
    for elem in puzzle:
        result += calc_min_cost(elem)
    return result


if __name__ == "__main__":
    print(solve_puzzle())
