f = open('Задание 26.txt')
k, n = map(int, f.readline().split())
# k = int(f.readline())
# n = int(f.readline())
a = []
for i in range(n):
    p, u = [int(s) for s in f.readline().split()]
    a.append((p, u))
a.sort()
d = [0] * k  # ячейки
m = 0
ans = 0
for i in range(n):
    p, u = a[i]
    for cell in range(k):
        if p > d[cell]:
            ans += 1
            d[cell] = u
            m = cell + 1
            print(d)
            break
print(d)
print(ans, m)
