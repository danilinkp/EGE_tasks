f = open('27B_6320.txt')
n, m = map(int, f.readline().split())
a = []
for i in range(n):
    k = int(f.readline())
    a.append(k)
a = a * 2

s = mx = sum(a[:2 * m + 1])
for i in range(m + 1, n + m):
    s = s - a[i - m - 1] + a[i + m]
    mx = max(mx, s)

print(mx)
