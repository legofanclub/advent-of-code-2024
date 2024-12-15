import math

f = open("input.txt", "r")

robots = []
for line in f:
    l = line.strip().split()
    p = tuple(int(x) for x in l[0][2:].split(","))
    v = tuple(int(x) for x in l[1][2:].split(","))
    robots.append((p, v))

width = 101
height = 103


def move_robots(robots):
    next_robots = []
    for (i, j), (di, dj) in robots:
        next_robots.append((((i + di) % width, (j + dj) % height), (di, dj)))
    return next_robots


def print_robot_map(robots):
    result = [[0] * width for _ in range(height)]
    for (i, j), _ in robots:
        result[j][i] += 1

    for line in result:
        print("".join("." if x == 0 else str(x) for x in line))


def get_string(robots):
    result = [[0] * width for _ in range(height)]
    for (i, j), _ in robots:
        result[j][i] += 1

    l = []
    for line in result:
        l += "".join(["." if x == 0 else str(x) for x in line]) + "\n"

    as_string = "".join(l)
    return as_string


string_versions = []
# the robot pattern loops and it repeats on the (101*103)th second
for i in range(101 * 103):
    robots = move_robots(robots)
    string_versions.append(get_string(robots))


def entropy(string):
    # from https://stackoverflow.com/a/2979208
    "Calculates the Shannon entropy of a string"

    # get probability of chars in string
    prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]

    # calculate the entropy
    entropy = -sum([p * math.log(p) / math.log(2.0) for p in prob])

    return entropy


# pattern is most regular when entropy is minimum
min_entropy = float("inf")
best = ""
best_i = 0
for i, sv in enumerate(string_versions):
    if entropy(sv) < min_entropy:
        min_entropy = entropy(sv)
        best = sv
        best_i = i

print(best)
print(best_i + 1)  # seconds start at 1
