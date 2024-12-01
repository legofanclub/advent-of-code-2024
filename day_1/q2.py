from collections import Counter

f = open("input.txt", "r")

firsts = []
seconds = []
for line in f:
    first, second = line.strip().split()
    firsts.append(int(first))
    seconds.append(int(second))

firsts.sort()
seconds.sort()

res = 0
d = Counter(seconds)

for x in firsts:
    if x in d:
        res += x * d[x]

print(res)
