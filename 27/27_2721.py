f = open('27B_2721.txt')
n = int(f.readline())
c = 0
k = 0
k_65 = 0
k_13 = 0
k_5 = 0
for i in range(n):
    x = int(f.readline())

    if x % 65 == 0:
        c += k
    elif x % 13 == 0:
        c += k_5
    elif x % 5 == 0:
        c += k_13
    else:
        c += k_65

    k += 1
    if x % 5 == 0:
        k_5 += 1
    if x % 13 == 0:
        k_13 += 1
    if x % 65 == 0:
        k_65 += 1

print(c)
