f = open('27B_2760.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = [[10 ** 20] * 107 for i in range(5)]
m = 10 ** 20
for i in range(n):
    g = i % 5
    ost = 0 if a[i] % 107 == 0 else 107 - a[i] % 107
    m = min(m, a[i] + k[g][ost])
    k[g][a[i] % 107] = min(a[i], k[g][a[i] % 107])

print(m)
