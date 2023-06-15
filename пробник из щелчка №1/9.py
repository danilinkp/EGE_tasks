import sys

c = 0
data = [i.split('\t') for i in map(str.strip, sys.stdin)]
for i in data:
    s = sorted([int(j) for j in i])
    if s[-1] < sum(s[:3]):
        if (s[0] + s[3] == s[1] + s[2]) or (s[0] + s[2] == s[3] + s[1]) or (s[0] + s[1] == s[3] + s[2]):
            print(s)
            c += 1

print(c)