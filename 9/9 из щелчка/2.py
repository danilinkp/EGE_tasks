import sys

c = 0
data = [i.split('\t') for i in map(str.strip, sys.stdin)]

for i in data:
    s = sorted([int(j) for j in i])
    if len(set(s)) == 5:
        if s[0] * 2 > s[-1]:
            c += 1
            print(s)


print(c)