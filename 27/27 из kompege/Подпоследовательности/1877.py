f = open('27B_1877.txt')
n = int(f.readline())
ms = 0
m = [10 ** 20] * 69
l = [0] * 69
ml = 0
s = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if s % 69 == 0:
        if s > ms:
            ms, ml = s, i + 1
    s1 = s - m[s % 69]
    l1 = (i + 1) - l[s % 69]
    if s1 > ms or (s1 == ms and l1 < ml):
        ms, ml = s1, l1

    if s < m[s % 69]:
        m[s % 69], l[s % 69] = s, i + 1

print(ms, ml)
