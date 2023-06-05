f = open('27A_2753.txt')
n = int(f.readline())
r = 7
a = [int(x) for x in f]
c = 0
k8 = [0] * 8
for i in range(1, n):
    ost = a[i - 1] % 8
    k8[ost] += 1
    if i > r:
        ost = a[i - (r + 1)] % 8
        k8[ost] -= 1
    ost2 = 0 if a[i] % 8 == 0 else 8 - a[i] % 8
    c += k8[ost2]


pairs = (n - r) * r + r * (r - 1) // 2
print(pairs - c)

#  да это жёстко
