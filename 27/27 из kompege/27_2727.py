f = open('27B_2727.txt')
n = int(f.readline())
c = 0
m = 10 ** 20
m_k = 10 ** 20
m_nk = 10 ** 20
for i in range(n):
    x = int(f.readline())
    if x % 31 == 0:
        m = min(x * min(m_nk, m_k), m)
        m_k = min(x, m_k)
    else:
        m = min(x * m_k, m)
        m_nk = min(x, m_nk)

print(m)

# халява :)
