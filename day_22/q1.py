def get_puzzle():
    f = open("input.txt", "r")

    puzzle = []
    for line in f:
        puzzle.append(int(line.strip()))

    return puzzle


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


def after_n_days(secret_num, n):
    for _ in range(n):
        secret_num = prune(mix(secret_num, secret_num * 64))
        secret_num = prune(mix(secret_num, secret_num // 32))
        secret_num = prune(mix(secret_num, secret_num * 2048))
    return secret_num


def solve():
    puzzle = get_puzzle()

    after_days = [after_n_days(value, 2000) for value in puzzle]

    return sum(after_days)


print(solve())
