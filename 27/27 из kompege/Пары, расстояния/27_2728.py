f = open('27B_2728.txt')
n = int(f.readline())
c = 0
m = -10 ** 20
k = [-10 ** 20] * 2
m_k_23 = 0
for i in range(n):
    x = int(f.readline())
    ost = 0 if x % 2 == 0 else 1
    if x % 23 == 0:
        m_k_23 = max(m_k_23, x)
    ost_23 = 0 if m_k_23 % 2 == 0 else 1
    m = max(m_k_23 + k[ost_23], m)

    k[x % 2] = max(x, k[x % 2])
print(m)

# хэштег изи
