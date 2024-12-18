# find the possible 6 digits to make num, for each digit, align them, then pick the only possible digits to get the answer


def pad(s):
    diff = 3 - len(s)
    return "0" * diff + s


def possible_6_digits_to_make_digit(n):
    cases = []
    # BBB is last 3 digits of A
    for last_3_a__bin_digits in range(8):
        BBB = pad(bin(last_3_a__bin_digits)[2:])
        CCC = pad(bin(n ^ int(BBB, 2) ^ 5 ^ 6)[2:])

        space = int(BBB, 2) ^ 5
        # space could be from 0 to 7
        if space >= 3:
            case = CCC + "x" * (space - 3) + BBB
            cases.append(case)
        elif space == 0:
            if BBB == CCC:
                case = "xxx" + BBB
                cases.append(case)
        elif space == 1:
            # first 2 digits of BBB must equal last 2 digits of CCC
            if BBB[0] == CCC[1] and BBB[1] == CCC[2]:
                case = "xx" + CCC + BBB[2]
                cases.append(case)
        elif space == 2:
            # first digit of BBB must equal last digit of CCC
            if BBB[0] == CCC[2]:
                case = "x" + CCC + BBB[1:]
                cases.append(case)

    cases.sort(key=lambda x: len(x))
    return cases


# because a is between 8 ** 15 and 8 ** 16 - 1 the number will have at most 16 base 8 digits or 48 binary digits
def big_pad(s, i):
    diff = 64 - len(s) - i * 3
    return "x" * diff + s + i * "x" * 3


def get_possible_values_for_each_digit():
    result = []
    for i, val in enumerate([2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 0, 5, 5, 3, 0]):
        possibilities = [
            "".join(big_pad(x, i)) for x in possible_6_digits_to_make_digit(val)
        ]
        result.append(possibilities)

    return list(reversed(result))


def get_numeric_value_of_string_with_x(s):
    l = list(s)

    for i in range(len(l)):
        if l[i] == "x":
            l[i] = "0"

    s = "".join(l)
    i = int(s, 2)

    return i


def can_merge(s1, s2):
    assert len(s1) == len(s2)

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        elif s1[i] == "x" or s2[i] == "x":
            continue
        else:
            return False
    return True


def merge(s1, s2):
    assert len(s1) == len(s2)

    merged = []
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            merged.append(s1[i])
        elif s1[i] == "x":
            merged.append(s2[i])
        elif s2[i] == "x":
            merged.append(s1[i])
        else:
            raise Exception("tried to merge 2 unmergable strings")

    return "".join(merged)


def dfs(rsf, depth, vals):
    # greedily add the smallest possiblity in each group to our solution
    if depth == 16:
        return rsf

    work = []
    for cur_string in vals[depth]:
        if can_merge(cur_string, rsf):
            new_string = merge(cur_string, rsf)
            work.append(new_string)

    # sort merged strings from smallest to largest
    work.sort(key=get_numeric_value_of_string_with_x)

    for new_string in work:
        res = dfs(new_string, depth + 1, vals)
        if res != None:
            return res

    return None


def solve():
    vals = get_possible_values_for_each_digit()

    soln_with_xs = dfs(
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", 0, vals
    )
    soln_with_xs_to_zeros = "".join(["0" if x == "x" else x for x in soln_with_xs])
    as_int = int(soln_with_xs_to_zeros, 2)
    return as_int


print(solve())
