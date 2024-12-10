f = open("input.txt", "r")

puzzle_input = ""
for line in f:
    puzzle_input = line.strip()

memory = []
for i, v in enumerate(puzzle_input):
    if i % 2 == 0:
        memory += [str(i//2)] * int(v)
    else:
        memory += ["."] * int(v)

l, r = 0, len(memory) - 1
while l < r:
    while memory[l] != ".":
        l += 1
    while memory[r] == ".":
        r -= 1
    if l >= r:
        break
    
    memory[l], memory[r] = memory[r], memory[l]

checksum = 0
for i in range(len(memory)):
    if memory[i] != ".":
        checksum += i * int(memory[i])
print(checksum)