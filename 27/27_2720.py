f = open('27B_2720.txt')
n = int(f.readline())
c = 0
k_7 = 0
for i in range(n):
    x = int(f.readline())

    if x % 7 == 0:
        c += i
        k_7 += 1
    if x % 7 != 0:
        c += k_7

print(c)
