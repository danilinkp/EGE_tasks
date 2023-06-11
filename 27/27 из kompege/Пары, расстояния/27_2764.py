f = open('27B_2764.txt')
n = int(f.readline())
a = [int(x) for x in f]
r = 7
m = 10 ** 20
k6 = [10 ** 20] * 23
k2 = [10 ** 20] * 23
k3 = [10 ** 20] * 23
kn6 = [10 ** 20] * 23
for i in range(r, n):
    ost = a[i - r] % 23
    if a[i - r] % 6 == 0:
        k6[ost] = min(a[i - r], k6[ost])
    elif a[i - r] % 3 == 0:
        k3[ost] = min(a[i - r], k3[ost])
    elif a[i - r] % 2 == 0:
        k2[ost] = min(a[i - r], k2[ost])
    else:
        kn6[ost] = min(a[i - r], kn6[ost])

    ost2 = 0 if a[i] % 23 == 0 else 23 - a[i] % 23
    if a[i] % 6 == 0:
        m = min(m, a[i] + min(kn6[ost2], k2[ost2], k3[ost2], k6[ost]))
    elif a[i] % 3 == 0:
        m = min(m, a[i] + min(k2[ost2], k6[ost2]))
    elif a[i] % 2 == 0:
        m = min(m, a[i] + min(k3[ost2], k6[ost2]))
    else:
        m = min(m, a[i] + k6[ost2])

print(m)
