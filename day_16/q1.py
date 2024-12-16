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


def get_fastest_time(puzzle, start_location, start_direction):
    # use Dijkstra's algorithm
    seen = set()
    first = (0, (start_location, start_direction))
    heap = [first]
    heapq.heapify(heap)

    while True:
        # pop min from heap
        counter, (location, direction) = heapq.heappop(heap)

        # check base cases
        if puzzle[location[0]][location[1]] == "#":
            continue
        elif puzzle[location[0]][location[1]] == "E":
            return counter
        elif (location, direction) in seen:
            continue

        seen.add((location, direction))

        # add children to heap
        go_straight = (counter + 1, (add_tuple(location, direction), direction))
        turn_clockwise = (
            counter + 1000,
            (
                location,
                (direction[1],-direction[0])
            ),
        )
        turn_counterclockwise = (
            counter + 1000,
            (location, (-direction[1], direction[0])),
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
    return get_fastest_time(puzzle, start, direction)


print(solve())
