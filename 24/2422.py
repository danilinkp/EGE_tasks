s = open('24_2422.txt').readline()
c = 1
m = 0
sub = ''
for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        c += 1
        sub += s[i]
        m = max(c, m)
    else:
        c = 1
        sub = ''
print(m, sub)
print('X' <= 'X')