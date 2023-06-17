f = open('27B_4713.txt')
n = int(f.readline())

a = []
sm = 0
for i in range(n):
    km, p = map(int, f.readline().split())
    k = p // 36 if p % 36 == 0 else p // 36 + 1
    sm += k
    a.append([km, k])

a.sort()
s = 0
for i in range(n):
    s += abs(a[i][0] - a[0][0]) * a[i][1]
mx = s
ex = 0
for i in range(1, n):
    ex += a[i - 1][1]
    r = a[i][0] - a[i - 1][0]
    s = s + r * ex - r * (sm - ex)
    mx = min(mx, s)

print(mx)
