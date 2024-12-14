import numpy as np
from sympy import Matrix
from sympy.solvers.diophantine import diophantine
from sympy.core.numbers import int_valued


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
            # q2 adds 10 trillion to x and y
            cur["prize"] = (
                int(x) + 10000000000000,
                int(y) + 10000000000000,
            )
    # add the last group if there's no trailing linebreak
    if len(cur) > 0:
        puzzle.append(cur)
    return puzzle


def calc_min_cost(elem):
    a_x, a_y = elem["a"]
    b_x, b_y = elem["b"]
    prize_x, prize_y = elem["prize"]

    A = Matrix([[a_x, b_x], [a_y, b_y]])
    b = Matrix([prize_x, prize_y])

    # solve with symbolic math to avoid numerical precision problems
    d = A.solve(b)
    if int_valued(d[0]) and int_valued(d[1]):
        return d[0] * 3 + d[1]
    return 0


def solve_puzzle():
    puzzle = get_puzzle()
    result = 0
    for elem in puzzle:
        result += calc_min_cost(elem)
    return result


if __name__ == "__main__":
    print(solve_puzzle())
