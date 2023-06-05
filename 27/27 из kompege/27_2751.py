f = open('27B_2751.txt')
n = int(f.readline())
r = 5
a = [int(x) for x in f]
c = 0
k13_0 = k13_1 = 0
k0 = k1 = 0
for i in range(r, n):
    if a[i - r] % 13 == 0 and a[i - r] % 2 == 0:
        k13_0 += 1
    if a[i - r] % 13 == 0 and a[i - r] % 2 != 0:
        k13_1 += 1
    if a[i - r] % 13 != 0 and a[i - r] % 2 == 0:
        k0 += 1
    if a[i - r] % 13 != 0 and a[i - r] % 2 != 0:
        k1 += 1

    if a[i] % 13 == 0 and a[i] % 2 == 0:
        c += k13_1 + k1
    if a[i] % 13 == 0 and a[i] % 2 != 0:
        c += k13_0 + k0
    if a[i] % 13 != 0 and a[i] % 2 == 0:
        c += k13_1
    if a[i] % 13 != 0 and a[i] % 2 != 0:
        c += k13_0


print(c)
