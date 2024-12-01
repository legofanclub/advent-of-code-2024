f = open("input.txt", "r")

firsts = []
seconds = []
for line in f:
    first, second = line.strip().split()
    firsts.append(int(first))
    seconds.append(int(second))

firsts.sort()
seconds.sort()

diff = 0
for i in range(len(firsts)):
    diff += abs(firsts[i] - seconds[i])

print(diff)
