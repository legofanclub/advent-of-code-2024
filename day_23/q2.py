from collections import defaultdict
import networkx as nx


def get_puzzle():
    f = open("input.txt", "r")

    d = defaultdict(list)
    for line in f:
        first, second = line.strip().split("-")
        d[first].append(second)
        d[second].append(first)

    return d


# find largest clique
def solve():
    puzzle = get_puzzle()

    # https://stackoverflow.com/a/66939446
    G = nx.Graph(puzzle)
    m = max(nx.algorithms.clique.find_cliques(G), key=len)

    return ",".join(sorted(m))


print(solve())
