import sys

c = 0
data = [i.split('\t') for i in map(str.strip, sys.stdin)]

for i in data:
    s = sorted([int(j) for j in i])
    if (all([n == 300 for n in s ])) or (sum(s) % 25 == 0):
        print(s)
        c += 1


print(c)

if all(n == 300 for n in [300, 300]):
    print('yep')