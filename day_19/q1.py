def get_puzzle():
    f = open("input.txt", "r")

    towels = f.readline().strip().split(", ")
    f.readline()

    designs = []
    for line in f:
        designs.append(line.strip())

    return towels, designs


def possible(design, towels):
    if design == "":
        return True

    for towel in towels:
        if len(towel) <= len(design) and design[: len(towel)] == towel:
            if possible(design[len(towel) :], towels):
                return True

    return False


def solve():
    towels, designs = get_puzzle()

    num_possible = 0
    for design in designs:
        if possible(design, towels):
            num_possible += 1

    return num_possible


print(solve())
