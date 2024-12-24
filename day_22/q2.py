# took < 52 minutes, could be sped up by using a hashmap instead of linear searching to find the 4 digit combinations
def get_puzzle():
    f = open("input.txt", "r")

    puzzle = []
    for line in f:
        puzzle.append(int(line.strip()))

    return puzzle


def mix(a, b):
    return a ^ b


def pad(n):
    diff = 32 - len(n)
    return "0" * diff + n


def prune(a):
    return a % 16777216


def after_n_days(secret_num, n):
    nums = []
    nums.append(secret_num)
    for i in range(n):
        secret_num = prune(mix(secret_num, secret_num * 64))
        secret_num = prune(mix(secret_num, secret_num // 32))
        secret_num = prune(mix(secret_num, secret_num * 2048))
        nums.append(secret_num)
    return nums


def get_diffs(l):
    diffs = []
    prev = l[0]

    l = [int(str(x)[-1]) for x in l]

    for val in l[1:]:
        diff = val - prev
        diffs.append(diff)
        prev = val
    return diffs


def get_last_4(diffs):
    last_4_s = []
    for i in range(0, len(diffs) - 3):
        last_4_s.append(",".join([str(x) for x in diffs[i : i + 4]]))
    return last_4_s


def num_banannas(seq, adpl4):
    total = 0
    for l, d in adpl4:
        for i, v in enumerate(d):
            if v == seq:
                total += int(str(l[i + 4])[-1])
                break
    return total


def solve():
    seen = set()
    puzzle = get_puzzle()
    after_days = [after_n_days(value, 2000) for value in puzzle]
    after_days_plus_last_4 = [(x, get_last_4(get_diffs(x))) for x in after_days]
    for l, d in after_days_plus_last_4:
        for v in d:
            seen.add(v)

    most_bananas = 0
    for seq in seen:
        most_bananas = max(most_bananas, num_banannas(seq, after_days_plus_last_4))

    return most_bananas


print(solve())
