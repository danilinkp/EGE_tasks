f = open('27B_2755.txt')
n = int(f.readline())
a = [int(x) for x in f]
m = 10 ** 20
k = [10 ** 20] * 144
for i in range(n):
    ost = 0 if a[i] % 144 == 0 else 144 - a[i] % 144
    if a[i] > k[ost]:
        m = min(a[i] + k[ost], m)

    k[a[i] % 144] = min(a[i], k[a[i] % 144])

print(m)
