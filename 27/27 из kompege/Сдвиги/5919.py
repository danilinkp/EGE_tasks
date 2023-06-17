f = open('27A_5919.txt')
n, k, v = map(int, f.readline().split())
a = [0] * k
sm = 0
for i in range(n):
    km, l = map(int, f.readline().split())
    km = km % k
    c = l // v if l % v == 0 else l // v + 1
    a[km] = c
s = 0
for i in range(k):
    s += min(i, k - i) * a[i]
mx = s
sm = sum(a)
forw = sum(a[1:k // 2 + 1])

# 0 -> 1 дешевле для 1..n//2
for i in range(1, k):
    s = s - forw + (sm - forw)
    if a[i] != 0:
        mx = min(mx, s)
    forw = forw - a[i] + a[(k // 2 + i) % k]
print(mx)
