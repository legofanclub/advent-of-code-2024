import heapq


def get_input():
    f = open("input.txt", "r")

    puzzle = []
    for line in f:
        puzzle.append(list(line.strip()))

    start = (-1, -1)
    for i, row in enumerate(puzzle):
        for j, val in enumerate(row):
            if val == "S":
                start = (i, j)
                break

    return puzzle, start


def add_tuple(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def get_tiles_on_fastest_path(puzzle, start_location, start_direction):
    # use Dijkstra's algorithm
    seen = {}
    path_so_far = set()
    first = (0, (start_location, start_direction, path_so_far))
    heap = [first]
    heapq.heapify(heap)
    min_length = float("inf")

    part_of_best_paths = set()

    while True:
        # pop min from heap
        counter, (location, direction, path_so_far) = heapq.heappop(heap)
        psf = path_so_far.copy()
        psf.add(location)

        # check base cases
        if puzzle[location[0]][location[1]] == "#":
            continue
        elif puzzle[location[0]][location[1]] == "E":
            if counter > min_length:
                return part_of_best_paths
            else:
                min_length = counter
                part_of_best_paths = part_of_best_paths | psf
        elif (location, direction) in seen and seen[(location, direction)] < counter:
            continue

        seen[(location, direction)] = counter

        # add children to heap
        go_straight = (counter + 1, (add_tuple(location, direction), direction, psf))
        turn_clockwise = (
            counter + 1000,
            (location,(direction[1],-direction[0],), psf)
        )
        turn_counterclockwise = (
            counter + 1000,
            (location, (-direction[1], direction[0]), psf),
        )

        heapq.heappush(heap, go_straight)
        heapq.heappush(heap, turn_clockwise)
        heapq.heappush(heap, turn_counterclockwise)


def pprint(puzzle):
    for line in puzzle:
        print("".join(line))


def solve():
    puzzle, start = get_input()
    direction = (0, 1)  # east
    tiles = get_tiles_on_fastest_path(puzzle, start, direction)
    return len(tiles)

print(solve())
