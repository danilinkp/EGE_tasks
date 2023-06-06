f = open('27A_2758.txt')
n = int(f.readline())
a = [int(x) for x in f]
r = 11
m = 10 ** 20
k = [10 ** 20] * 2142
for i in range(1, n):
    ost = a[i - 1] % 2142
    k[ost] = min(k[ost], a[i - 1])
    if i > r:
        ost = a[i - (r + 1)] % 2142
        k[ost] = 10 ** 20
    ost2 = 0 if a[i] % 2142 == 0 else 2142 - a[i] % 2142
    m = min(m, a[i] + k[ost2])

print(m)
