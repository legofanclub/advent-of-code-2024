from collections import defaultdict
from functools import cmp_to_key
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

def custom_comparison(first, second):
    should_be_after_first = d[first]
    should_be_after_second = d[second]

    # negative when left should be first
    if second in should_be_after_first:
        return -1

    # positive when right should be first
    elif first in should_be_after_second:
        return 1

    # zero if it doesn't matter
    return 0


def sort_line(line):
    return list(sorted(line, key=cmp_to_key(custom_comparison)))

result = 0
for line in puzzle_input:
    if not is_good(line):
        fixed = sort_line(line)
        result += int(fixed[len(fixed)//2])

print(result)