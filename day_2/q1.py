f = open("input.txt", "r")

input_arr = []
for line in f:
    ints = [int(x) for x in line.strip().split()]
    input_arr.append(ints)

def gradually_increasing(l):
    prev = l[0]
    for val in l[1:]:
        if val > prev + 3 or val < prev + 1:
            return False
        prev = val
    
    return True

def gradually_decreasing(l):
    prev = l[0]
    for val in l[1:]:
        if val < prev - 3 or val > prev - 1:
            return False
        prev = val

    return True

res = 0
for line in input_arr:
    if gradually_increasing(line) or gradually_decreasing(line):
        res += 1

print(res)
