f = open('27B_2726.txt')
n = int(f.readline())
c = 0
m = -10 ** 20
k = [-10 ** 20] * 2
for i in range(n):
    x = int(f.readline())
    ost = 1 if x % 2 == 0 else 0
    m = max(x + k[ost], m)

    k[x % 2] = max(x, k[x % 2])
print(m)

# да я генний :)
