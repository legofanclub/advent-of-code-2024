f = open("input.txt", "r")

stones = []
for line in f:
    stones = [int(x) for x in line.strip().split()]


def blink(stone):
    if stone == 0:
        return [1]
    as_str = str(stone)
    if len(as_str) % 2 == 0:
        return [int(as_str[: len(as_str) // 2]), int(as_str[len(as_str) // 2 :])]
    else:
        return [stone * 2024]


for _ in range(25):
    new_stones = []
    for stone in stones:
        new_stones += blink(stone)
    stones = new_stones

print(len(new_stones))
