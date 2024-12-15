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


for _ in range(100):
    robots = move_robots(robots)

# count robots in each quadrant
q1, q2, q3, q4 = 0, 0, 0, 0
for (i, j), _ in robots:
    if i < width // 2 and j < height // 2:  # 0 to 4
        q2 += 1
    elif i < width // 2 and j > (height // 2):
        q3 += 1
    elif i > width // 2 and j < height // 2:
        q1 += 1
    elif i > width // 2 and j > (height // 2):
        q4 += 1


def print_robot_map():
    result = [[0] * width for _ in range(height)]
    for (i, j), _ in robots:
        result[j][i] += 1

    for line in result:
        print("".join(str(x) for x in line))


print(q1 * q2 * q3 * q4)
