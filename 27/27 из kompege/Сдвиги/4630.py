f = open('27A_4630.txt')
n, k, m = map(int, f.readline().split())
a = []
for i in range(n):
    km, p = map(int, f.readline().split())
    c = p // 9 if p % 9 == 0 else p // 9 + 1
    a.append([km, c])

a = sorted(a, key=lambda x: x[0])
b = [0] * 100000
for i in range(n):
    km, c = a[i]
    b[km] = c

mx = s = sum(b[:2 * m + 1])
for i in range(m + 1, 100000 - m):
    s = s - b[i - m - 1] + b[i + m]
    if b[i] > 0:
        mx = max(mx, s)

print(mx)
