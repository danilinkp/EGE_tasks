import sys

c = 0
data = [i.split('\t') for i in map(str.strip, sys.stdin)]
for i in data:
    s = sorted([int(j) for j in i])
    if len(set(s)) == 5:
        if 2 * (s[0] + s[4]) <= sum(s[1:4]):
            c += 1

print(c)