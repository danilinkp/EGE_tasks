f = open('Задание 24.txt').readlines()
m = 10 ** 20
s = ''
for i in f:
    if len(i[:-1]) < m:
        m = len(i[:-1])
        s = i
c = 0
for i in range(m // 2):
    if s[i] == s[m - i - 1]:
        c += 1

print(c)

