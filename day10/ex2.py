from operator import sub
from collections import Counter

with open('input.txt') as f:
    data = [0] + sorted(int(x) for x in f)
    data.append(data[-1] + 3)

paths = [0] * (len(data) - 1) + [1]
for i in range(len(data) - 2, -1, -1):
    for j in range(i + 1, i + 4):
        if j < len(data) and data[j] - 3 <= data[i]:
            paths[i] += paths[j]

print("total number of distinct ways the adapters can be arranged to connect the charging outlet to the device -",paths[0])