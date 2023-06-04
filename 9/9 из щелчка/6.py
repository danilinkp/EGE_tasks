import sys
from itertools import permutations

c = 0
data = [i.split('\t') for i in map(str.strip, sys.stdin)]

for i in data:
    s = sorted([int(j) for j in i])
    if all([sum(i) % 2 == 0 for i in list(permutations(s, r=2))]):
        c += 1
        print(s)


print(c)


