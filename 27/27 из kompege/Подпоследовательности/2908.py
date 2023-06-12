f = open('27B_2908.txt')
n = int(f.readline())
q = []
s = 0
k7 = 0
for i in range(6):
    x = int(f.readline())
    s += x
    if x % 7 == 0 and x > 0:
        k7 += 1
    q.append([s, k7])

ms = -10 ** 20
m = [10 ** 20] * 7
for i in range(n - 6):
    x = int(f.readline())
    s += x
    if x % 7 == 0 and x > 0:
        k7 += 1
    if k7 % 7 == 0:
        ms = max(ms, s)
    s1 = s - m[k7 % 7]
    ms = max(ms, s1)
    s0, k0 = q[0]
    m[k0 % 7] = min(m[k0 % 7], s0)
    q.pop(0)
    q.append([s, k7])

print(ms)
