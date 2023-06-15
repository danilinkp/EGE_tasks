f = open('Задание 17.txt')
a = [int(x) for x in f]
print(len(a))
c = 0
ms = 0
for i in range(len(a) - 1):
    if len(str(a[i] * a[i + 1])) > 1 and str(a[i] * a[i + 1])[1] == '4':
        c += 1
        if (a[i] + a[i + 1]) % 24 == 0:
            ms = max(ms, a[i] + a[i + 1])
print(c, ms)
print(c + ms)