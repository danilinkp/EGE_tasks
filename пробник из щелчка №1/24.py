s = open('Задание 24.txt').readline()
s = s.replace('OSR', '*').replace('RSO', '*')
s = s.replace('R', 'S').replace('O', 'S').replace('S', ' ')
print(max(len(i) for i in s.split()))

# # 2 способ
c = m = 0
pairs = ['OSR', 'RSO']
for i in range(0, len(s) - 2, 3):
    if s[i] + s[i + 1] + s[i + 2] in pairs:
        c += 1
        m = max(c, m)
    else:
        c = 0

print(m)