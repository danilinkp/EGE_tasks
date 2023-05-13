f = open('27A_2722.txt')
n = int(f.readline())
c = 0
k_5 = k_ev = k_odd = k_5_ev = k_5_odd = 0
for i in range(n):
    x = int(f.readline())
    if x % 5 == 0 and x % 2 == 0:
        k_5_ev += 1
        k_ev += 1
        c += k_odd
    elif x % 5 == 0 and x % 2 != 0:
        k_5_odd += 1
        k_odd += 1
        c += k_ev
    elif x % 2 == 0:
        k_ev += 1
        c += k_5_odd
    else:
        k_odd += 1
        c += k_5_ev
print(c)
