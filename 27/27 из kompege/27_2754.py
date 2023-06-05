f = open('27A_2755.txt')
n = int(f.readline())
a = [int(x) for x in f]
r = 5
m = -10 ** 20
k = [-10 ** 20] * 137
for i in range(r, n):
    ost = a[i - r] % 137
    k[ost] = max(a[i - r], k[ost])

    ost2 = a[i] % 137
    if a[i] > k[ost2]:
        m = max(a[i] - k[ost2], m)
    else:
        m = max(k[ost] - a[i], m)

print(m)
print(k)