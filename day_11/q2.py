from functools import cache

f = open("input.txt", "r")

stones = []
for line in f:
    stones = [int(x) for x in line.strip().split()]


# caching makes it so that every unique stone on the ith layer only has to be done once
@cache
def blink(stone: int, i):
    if i == 0:
        return 1
    if stone == 0:
        return blink(1, i - 1)
    as_str = str(stone)
    if len(as_str) % 2 == 0:
        first_half = int(as_str[: len(as_str) // 2])
        second_half = int(as_str[len(as_str) // 2 :])
        return blink(first_half, i - 1) + blink(second_half, i - 1)
    else:
        return blink(stone * 2024, i - 1)


num_stones = 0
for stone in stones:
    num_stones += blink(stone, 75)

print(num_stones)
