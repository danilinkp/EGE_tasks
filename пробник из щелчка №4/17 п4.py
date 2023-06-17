f = open('Задание 17.txt')
a = [int(x) for x in f]
m = max([i for i in a if i % 171 == 0])
c = 0
ms = 0

for i in range(len(a) - 1):
    if (a[i] < m or a[i + 1] < m) and (a[i] % 2 != 0 or a[i + 1] % 2 != 0):
        c += 1
        ms = max(ms, a[i] + a[i + 1])
print(c, ms)