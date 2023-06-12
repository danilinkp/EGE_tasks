f = open('27B_2902.txt')
n = int(f.readline())
m = [0] * 11
k_n = 0
c_p = 0
for i in range(n):
    x = int(f.readline())
    if x % 5 == 0:
        k_n += 1
    if k_n % 11 == 0:
        c_p += 1
    c_p += m[k_n % 11]
    m[k_n % 11] += 1

print(c_p)
