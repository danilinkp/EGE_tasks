f = open('27A_2900.txt')
n = int(f.readline())
ms = 0
m = [0] * 666
s = 0
c = 0
for i in range(n):
    x = int(f.readline())
    s += x
    s1 = s - m[s % 1000]
    ms = max(ms, s1)
    m[s % 1000] = min(m[s % 1000], s)

print(ms)
