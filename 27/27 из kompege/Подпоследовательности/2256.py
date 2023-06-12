f = open('27B_2256.txt')
n = int(f.readline())
m = [10 ** 20] * 3
s = 0
ms = 0
k = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if x % 5 == 0:
        k += 1
    if k % 3 == 0:
        ms = max(ms, s)
    s1 = s - m[k % 3]
    ms = max(ms, s1)
    m[k % 3] = min(m[k % 3], s)

print(ms)
