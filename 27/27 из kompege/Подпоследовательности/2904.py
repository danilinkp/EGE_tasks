f = open('27B_2904.txt')
n = int(f.readline())
ms = 10 ** 20
m = [-10 ** 20] * 2077
l = [0] * 2077
ml = 0
s = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if s % 2077 == 0:
        if s < ms:
            ms, ml = s, i + 1
    s1 = s - m[s % 2077]
    l1 = (i + 1) - l[s % 2077]
    if s1 < ms or (s1 == ms and l1 > ml):
        ms, ml = s1, l1

    if s > m[s % 2077]:
        m[s % 2077], l[s % 2077] = s, i + 1

print(ms, ml)
