f = open('27B_2901.txt')
n = int(f.readline())
m = [0] * 11
k_n = 0
s = 0
c_p = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if x % 5 == 0:
        k_n += 1
    if k_n % 11 == 0:
        c_p += 1
    s1 = s - m[k_n % 11]
    c_p += 1
    m[k_n % 7] = s


print(c_p)
