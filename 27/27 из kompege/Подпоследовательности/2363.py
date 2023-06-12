f = open('27B_2363.txt')
n = int(f.readline())
q = []
s = 0

for i in range(4):
    x = int(f.readline())
    s += x
    q.append(s)

k = [0] * 117
c = 0
for i in range(n - 4):
    x = int(f.readline())
    s += x
    if s % 117 == 0:
        c += 1
    c += k[s % 117]
    k[q[0] % 117] += 1
    q.pop(0)
    q.append(s)

print(c)