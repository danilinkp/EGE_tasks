f = open('27B_2761.txt')
n = int(f.readline())
r = 6
a = [int(x) for x in f]
c = 0
k13_0 = [0] * 13
k13_1 = [0] * 13
for i in range(r, n):
    ost = a[i - r] % 13
    if a[i - r] % 2 == 0:
        k13_0[ost] += 1
    else:
        k13_1[ost] += 1
    ost2 = a[i] % 13
    if a[i] % 2 == 0:
        c += k13_0[ost2] + k13_1[ost2]
    else:
        c += k13_0[ost2]
print(c)
