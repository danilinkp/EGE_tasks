f = open('27B_2757.txt')
n = int(f.readline())
r = 9
a = [int(x) for x in f]
c = 0
k23 = 0
k1 = 0
for i in range(r, n):
    if a[i - r] % 23 == 0:
        k23 += 1
    if a[i - r] % 23 != 0:
        k1 += 1

    if a[i] % 23 == 0:
        c += k23 + k1
    if a[i] % 23 != 0:
        c += k23
print(c)
