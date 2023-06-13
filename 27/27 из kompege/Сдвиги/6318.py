f = open('27A_6318.txt')
n, m = map(int, f.readline().split())
a = []
for i in range(n):
    k = int(f.readline())
    a.append(k)
s = mx = sum(a[:2 * m + 1])
for i in range(m + 1, n - m):
    s = s - a[i - m - 1] + a[i + m]
    mx = max(mx, s)

print(mx)
