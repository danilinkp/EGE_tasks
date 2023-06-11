f = open('27B_2754.txt')
n = int(f.readline())
a = [int(x) for x in f]
r = 5
m = -10 ** 20
k = [-10 ** 20] * 137
for i in range(r, n):
    ost = a[i - r] % 137
    k[ost] = max(a[i - r], k[ost])

    ost2 = a[i] % 137
    m = max(k[ost2] - a[i], m)

print(m)
