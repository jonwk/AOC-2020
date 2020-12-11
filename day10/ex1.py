from operator import sub
from collections import Counter

with open('input.txt') as f:
    data = [0] + sorted(int(x) for x in f)
    data.append(data[-1] + 3)

diffs = map(sub, data[1:], data)
count = Counter(diffs)
print("the number of 1-jolt differences multiplied by the number of 3-jolt differences -",count[1] * count[3])
