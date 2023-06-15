f = open('Задание 27B.txt')
n, k = map(int, f.readline().split())
a = [int(x) for x in f]
ms = 0
m1 = 0
for i in range(k, n):
    m1 = max(a[i - k], m1)
    ms = max(m1 + a[i], ms)

print(ms)
