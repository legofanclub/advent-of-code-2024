from collections import defaultdict


def get_puzzle():
    f = open("input.txt", "r")

    d = defaultdict(list)
    for line in f:
        first, second = line.strip().split("-")
        d[first].append(second)
        d[second].append(first)

    return d


def solve():
    puzzle = get_puzzle()

    result = set()
    for node, neighbors in puzzle.items():

        for neighbor in neighbors:
            for nn in puzzle[neighbor]:
                if nn in neighbors:
                    l = [node, neighbor, nn]
                    l.sort()
                    result.add(tuple(l))

    result = [x for x in result if len([z for z in x if z[0] == "t"]) > 0]

    return len(result)


print(solve())
