f = open('Задание 27B.txt')
n, v = map(int, f.readline().split())

a = []
sm = 0
for i in range(n):
    km, p = map(int, f.readline().split())

    k = p // v if p % v == 0 else p // v + 1
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
