f = open('27B_2752.txt')
n = int(f.readline())
r = 6
a = [int(x) for x in f]
c = 0
k3 = 0
k1 = 0
k7 = 0
k9 = 0
for i in range(r, n):
    if a[i - r] % 10 == 3:
        k3 += 1
    if a[i - r] % 10 == 1:
        k1 += 1
    if a[i - r] % 10 == 7:
        k7 += 1
    if a[i - r] % 10 == 9:
        k9 += 1

    if a[i] % 10 == 1:
        c += k3
    if a[i] % 10 == 3:
        c += k1
    if a[i] % 10 == 7:
        c += k9
    if a[i] % 10 == 9:
        c += k7
print(c)
