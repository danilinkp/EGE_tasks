f = open('27A_4116.txt')
n, k = map(int, f.readline().split())
a = [int(x) for x in f]
s = 0
c = 0

while (s + a[c]) < k:
    s += a[c]
    c += 1
mk = j = c
st = 0

for i in range(j, n):
    s -= a[st]
    st += 1
    while c != n and (s + a[c]) <= k:
        s += a[c]
        c += 1
    mk = max(mk, c - st)

print(mk)
