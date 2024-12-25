def get_puzzle():
    f = open("input.txt", "r")

    clauses = {}
    for line in f:
        if line == "\n":
            break
        first, second = line.strip().split(": ")
        clauses[first] = ("exact", int(second), int(second))

    zs = []
    for line in f:
        i1, type, i2, _, out = line.strip().split()
        clauses[out] = (type, i1, i2)
        if out[0] == "z":
            zs.append(out)

    zs.sort(reverse=True)

    return clauses, zs


def determine_state(name, clauses):
    type, i1, i2 = clauses[name]
    if type == "exact":
        return i1
    elif type == "OR":
        return determine_state(i1, clauses) | determine_state(i2, clauses)
    elif type == "AND":
        return determine_state(i1, clauses) & determine_state(i2, clauses)
    elif type == "XOR":
        return determine_state(i1, clauses) ^ determine_state(i2, clauses)


def solve():
    clauses, zs = get_puzzle()

    a = []
    for z in zs:
        a.append(str(determine_state(z, clauses)))

    print("".join(a))
    return int("".join(a), 2)


print(solve())
