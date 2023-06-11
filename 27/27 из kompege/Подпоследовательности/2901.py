f = open('27B_2901.txt')
n = int(f.readline())
k = [0] * 666
s = 0
c = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if s % 666 == 0:
        c += 1
    c += k[s % 666]
    k[s % 666] += 1

print(c)
