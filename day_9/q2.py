f = open("input.txt", "r")

puzzle_input = ""
for line in f:
    puzzle_input = line.strip()

memory = []
for i, v in enumerate(puzzle_input):
    if i % 2 == 0:
        memory.append((str(i//2), int(v)))
    else:
        memory.append((".", int(v)))

for l in range(len(memory)):
    if memory[l][0] != '.':
        continue

    gap_size = memory[l][1]

    for r in range(len(memory) -1, l, -1):
        if memory[r][0] == ".":
            continue
        
        block_val = memory[r][0]
        block_size = memory[r][1]

        # move block to gap
        if block_size <= gap_size:
            new_gap_size = gap_size - block_size
            if new_gap_size == 0:
                memory[l], memory[r] = memory[r], memory[l]
            else:
                memory[l], memory[r] = memory[r], ('.', memory[r][1])
                memory.insert(l+1, ('.', new_gap_size)) # add new gap after filling in block
            break

result_list = [[x[0]]*int(x[1]) for x in memory]
result_list = [x for sublist in result_list for x in sublist] # flattten 2d result list

checksum = 0
for i, v in enumerate(result_list):
    if v != ".":
        checksum += i * int(v)
print(checksum)