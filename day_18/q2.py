from collections import deque


def get_puzzle():
    f = open("input.txt", "r")
    coords = []
    for line in f:
        coord = [int(x) for x in line.strip().split(",")]
        coord = (coord[1], coord[0])  # switch from (x,y) to (y,x)
        coords.append(coord)

    map_size = 71
    memory = [["."] * map_size for _ in range(map_size)]

    return coords, memory


def tuple_add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def inbounds(tup, m):
    return 0 <= tup[0] < len(m) and 0 <= tup[1] < len(m[0])


def bfs(coord, memory, destination):
    q = deque([(coord, 0)])
    seen = set()

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while len(q) > 0:
        cur, level = q.popleft()
        if cur in seen or not inbounds(cur, memory) or memory[cur[0]][cur[1]] == "#":
            continue
        seen.add(cur)
        if cur == destination:
            return level

        for d in directions:
            new_location = tuple_add(cur, d)
            q.append((new_location, level + 1))


def pprint(m):
    for line in m:
        print("".join(line))


def solve():
    # could binary search but brute force should also work and take <=90s
    coords, memory = get_puzzle()

    for coord in coords:
        memory[coord[0]][coord[1]] = "#"
        shortest_path_length = bfs((0, 0), memory, (70, 70))
        if shortest_path_length == None:
            return (coord[1], coord[0])  # swap to use (x,y) convention


print(solve())
