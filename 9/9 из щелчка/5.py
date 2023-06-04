import sys

c = 0
data = [i.split('\t') for i in map(str.strip, sys.stdin)]

for i in data:
    s = sorted([int(j) for j in i])
    if ((s[1] * s[2]) % 10 == 7) or ((s[0] * s[2]) % 10 == 7) or ((s[1] * s[0]) % 10 == 7):
        c += 1
        print(s)


print(c)





