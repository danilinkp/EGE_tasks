f = open('27B_2733.txt')
n = int(f.readline())
c = 0
m = 80
b = 50000
k = [0] * m
k_b = [0] * m
for i in range(n):
    x = int(f.readline())
    ost = 0 if x % m == 0 else m - x % m
    if x > 50000:
        c += k[ost]
        k_b[x % m] += 1
    if x <= 50000:
        c += k_b[ost]
    k[x % m] += 1
print(c)
