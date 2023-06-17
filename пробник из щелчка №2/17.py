f = open('Задание 17.txt')
a = [int(x) for x in f]
c = 0
ms = 0

for i in range(len(a) - 2):
    tri = [a[i], a[i + 1], a[i + 2]]
    if any([el % 3 == 0 for el in tri]) and sum(tri) % 2 == 0 and (tri[1] > (sum(tri) / 3)):
        c += 1
        ms = max(ms, sum(tri))

print(c, ms)