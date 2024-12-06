from collections import defaultdict
f = open("input.txt", "r")

d = defaultdict(list)

for line in f:
    if line == "\n":
        break
    first, second = line.strip().split("|")
    d[first].append(second)

puzzle_input = []
for line in f:
    puzzle_input.append(line.strip().split(","))

def is_good(line):
    seen = set()
    for val in line:
        bad_if_before = d[val]

        for bad in bad_if_before:
            if bad in seen:
                return False

        seen.add(val)
    
    return True

result = 0
for line in puzzle_input:
    if is_good(line):
        result += int(line[len(line)//2])

print(result)