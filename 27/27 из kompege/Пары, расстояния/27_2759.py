f = open('27B_2759.txt')
n = int(f.readline())
a = [int(x) for x in f]
k = [0] * 134

c = 0
for i in range(n):
    if a[i] < 134:
        for j in range(a[i] + 1, 134):
            if a[i] + j <= 134:
                c += k[j]

        k[a[i]] += 1



print(c)
