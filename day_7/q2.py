f = open("input.txt", "r")

puzzle = []
for line in f:
    contents = line.strip().split()
    first = contents[0][:-1]
    rest = contents[1:]

    puzzle.append((int(first), [int(x) for x in rest]))

def is_valid(target, values, rsf):
    if values == [] and target == rsf:
        return True
    elif values:
        first = values[0]
        return is_valid(target, values[1:], rsf * first) or is_valid(target, values[1:], rsf + first) or is_valid(target, values[1:], int(str(rsf) + str(first)))
    else:
        return False

result = 0
for line in puzzle:
    target = line[0]
    values = line[1]
    
    if is_valid(target, values, 0):
        result += target

print(result)