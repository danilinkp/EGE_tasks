s = open('24_5171.txt').readline()
c = m = 0
for j in range(2):
    for i in range(j, len(s) - 1, 2):
        if s[i] + s[i + 1] == 'CA':
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)