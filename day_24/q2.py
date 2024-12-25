def get_puzzle():
    f = open("input.txt", "r")

    clauses = {}
    for line in f:
        if line == "\n":
            break
        first, second = line.strip().split(": ")
        clauses[("exact", int(second), int(second))] = first

    zs = []
    for line in f:
        i1, type, i2, _, out = line.strip().split()

        # ensure consistent order of clauses
        l = list(sorted([i1, i2]))
        clauses[(type, l[0], l[1])] = out
        if out[0] == "z":
            zs.append(out)

    zs.sort(reverse=True)

    return clauses, zs


def solve():
    clauses, _ = get_puzzle()

    # for every pair of bits, check that they match the full adder schematic, fix them manually and rerun
    #   eg. x00 AND y00 -> a
    #       x00 XOR y00 -> x
    #       x XOR c = s
    #       x AND c = i
    #       i OR a = new_c

    carry = None
    for i in range(45):
        s = str(i)
        diff = 2 - len(s)
        x_dig = "x" + "0" * diff + s
        y_dig = "y" + "0" * diff + s
        print(f"x_dig is: {x_dig}")
        print(f"y_dig is: {y_dig}")
        assert ("AND", x_dig, y_dig) in clauses
        a = clauses[("AND", x_dig, y_dig)]
        assert ("XOR", x_dig, y_dig) in clauses
        print(f"a is: {a}")
        x = clauses[("XOR", x_dig, y_dig)]
        print(f"x is: {x}")
        if carry:
            print(f"carry is {carry}")
            # account for order
            l = list(sorted([x, carry]))
            print(l)
            assert ("XOR", l[0], l[1]) in clauses
            s = clauses[("XOR", l[0], l[1])]
            assert ("AND", l[0], l[1]) in clauses
            i = clauses[("AND", l[0], l[1])]
            print(f"s is: {s}")
            print(f"i is {i}")

            l2 = list(sorted([i, a]))
            assert ("OR", l2[0], l2[1]) in clauses
            carry = clauses[("OR", l2[0], l2[1])]
        else:
            carry = clauses[("AND", x_dig, y_dig)]


print(solve())
