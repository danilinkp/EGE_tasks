f = open('27A_2759.txt')
n = int(f.readline())
a = [int(x) for x in f]
m = -10 ** 20
k = [-10 ** 20] * 100
for i in range(n):
    ost = 12 - a[i] % 100 if a[i] % 100 < 13 else 112 - a[i] % 100
    if a[i] < k[ost]:
        m = max(a[i] + k[ost], m)
    k[a[i] % 100] = max(a[i], k[a[i] % 100])

print(m)
