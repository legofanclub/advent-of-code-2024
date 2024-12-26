def get_puzzle():
    f = open("input.txt", "r")

    puzzle = []
    cur = []
    for line in f:
        if line == "\n":
            puzzle.append(cur)
            cur = []
        else:
            cur.append(line.strip())
    puzzle.append(cur)
    return puzzle


def get_keys_and_locks(puzzle):
    locks = []
    keys = []
    for entry in puzzle:
        if entry[0] == "#####":
            locks.append(entry)
        else:
            keys.append(entry)
    return keys, locks


def keys_to_num(keys):
    result = []
    for key in keys:
        cur = []
        for i in range(0, 5):
            for j in reversed(range(0, 7)):
                if key[j][i] == ".":
                    cur.append(5 - j)
                    break
        result.append(cur)
    return result


def locks_to_num(locks):
    result = []
    for lock in locks:
        cur = []
        for i in range(0, 5):
            for j in range(0, 7):
                if lock[j][i] == ".":
                    cur.append(j - 1)
                    break
        result.append(cur)
    return result


def fit(lock, key):
    for i in range(5):
        if lock[i] + key[i] > 5:
            return False
    return True


def solve():
    puzzle = get_puzzle()

    keys, locks = get_keys_and_locks(puzzle)
    keys_as_nums = keys_to_num(keys)
    locks_as_nums = locks_to_num(locks)

    result = 0
    for lock in locks_as_nums:
        for key in keys_as_nums:
            if fit(lock, key):
                result += 1

    return result


print(solve())
