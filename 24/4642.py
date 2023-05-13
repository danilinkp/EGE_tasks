s = open('24_4642.txt').readline()
c = m = 0
pairs = ['A1', 'A2', 'B1', 'B2']
for j in range(2):
    for i in range(j, len(s) - 1, 2):
        if s[i] + s[i + 1] in pairs:
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)