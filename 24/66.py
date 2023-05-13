# -*- coding: utf-8 -*-


s = open('24_66.txt').readline()
c = m = 0
for j in range(3):
    for i in range(j, len(s) - 2, 3):
        if s[i] + s[i + 1] + s[i + 2] == 'KOT':
            c += 1
            m = max(m, c)
        else:
            c = 0

print(m)
