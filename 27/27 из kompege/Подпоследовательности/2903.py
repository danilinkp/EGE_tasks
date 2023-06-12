f = open('27B_2903.txt')
n = int(f.readline())
m = [-10 ** 20] * n
s = 0
ms = 10 ** 20
k = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if x % 3 == 0:
        k += 1
    if k == 10:
        ms = min(ms, s)
    s1 = s - m[k - 10]
    ms = min(ms, s1)
    m[k] = max(m[k], s)

print(ms)
