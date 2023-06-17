f = open('27_B_3587.txt')
n = int(f.readline())
a = []
sm = 0
for i in range(n):
    k = int(f.readline())
    sm += k
    a.append(k)
a = a * 2
s = 0
for i in range(n):
    s += min(i, n - i) * a[i]
mx = s

m_km = 0

# 0 -> 1 дешевле для 1..n//2
cheaper = sum(a[1:n // 2 + 1])

for i in range(1, n):
    s = s - cheaper + (sm - cheaper)
    if s < mx:
        mx = s
        m_km = i + 1
    cheaper = cheaper - a[i] + a[n // 2 + i]

print(m_km)
