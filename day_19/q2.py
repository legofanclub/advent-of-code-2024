from functools import cache


def get_puzzle():
    f = open("input.txt", "r")

    towels = f.readline().strip().split(", ")
    f.readline()

    designs = []
    for line in f:
        designs.append(line.strip())

    return towels, designs


@cache
def possible(design, towels):
    if design == "":
        return 1

    num_ways = 0
    for towel in towels:
        if len(towel) <= len(design) and design[: len(towel)] == towel:
            num_ways += possible(design[len(towel) :], towels)

    return num_ways


def solve():
    towels, designs = get_puzzle()

    num_possible = 0
    for design in designs:
        num_possible += possible("".join(design), tuple(towels))

    return num_possible


print(solve())
