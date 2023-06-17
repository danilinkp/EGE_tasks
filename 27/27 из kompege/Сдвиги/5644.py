f = open('27B_5644.txt')
n = int(f.readline())
a = []
sm = 0
for i in range(n):
    k = int(f.readline())
    sm += k
    a.append(k)

s = 0
for i in range(n):
    s += i * a[i]
mx = s

expen = 0
for i in range(1, n):
    expen += a[i - 1]
    s = s + expen - (sm - expen)
    mx = max(mx, s)

print(mx)
