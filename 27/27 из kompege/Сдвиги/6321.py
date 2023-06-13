f = open('27B_6321.txt')
n, v, m = map(int, f.readline().split())
a = []
for i in range(n):
    km, k = map(int, f.readline().split())
    c = k // v if k % v == 0 else k // v + 1
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

# АЛЬТЕРНАТИВНЫЙ МЕТОД РЕШЕНИЯ. МЕТОД ДВУХ УКАЗАТЕЛЕЙ
st = end = 0
s = a[0][1]
while a[end + 1][0] - a[0][0] <= m:
    end += 1
    s += a[end][1]
mx = s
for i in range(1, n):
    while end != n - 1 and a[end + 1][0] - a[i][0] <= m:
        end += 1
        s += a[end][1]
    while a[i][0] - a[st][0] > m:
        s -= a[st][1]
        st += 1
    mx = max(mx, s)

print(mx)