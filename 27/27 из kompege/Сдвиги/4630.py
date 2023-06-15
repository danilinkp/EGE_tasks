f = open('27B_4630.txt')
n, k, m = map(int, f.readline().split())
a = []
for i in range(n):
    km, p = map(int, f.readline().split())
    km = km % k
    c = p // 9 if p % 9 == 0 else p // 9 + 1
    a.append([km, c])

b = [0] * (k + 1)
for i in range(n):
    km, c = a[i]
    b[km] = c

b = b * 2  # make a ring :)

mx = s = sum(b[:2 * m + 1])
for i in range(m + 1, k + m):
    s = s - b[i - m - 1] + b[i + m]
    if b[i] > 0:
        mx = max(mx, s)

print(mx)
