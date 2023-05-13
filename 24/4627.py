s = open('24_4627.txt').readline()
c = m = 0
pairs = ['NPO', 'PNO']
for j in range(3):
    for i in range(j, len(s) - 2, 3):
        if s[i] + s[i + 1] + s[i + 2] in pairs:
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)