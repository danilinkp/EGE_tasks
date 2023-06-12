f = open('27A_2907.txt')
n = int(f.readline())
m = [10 ** 20] * 30
s = 0
ms = -10 ** 20
k = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if x % 2 == 0 and x > 0:
        k += 1
    if k % 30 == 0:
        ms = max(ms, s)
    s1 = s - m[k % 30]
    ms = max(ms, s1)
    m[k % 30] = min(m[k % 30], s)

print(ms)
