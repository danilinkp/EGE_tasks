s = open('24_2427.txt').readline()
m = c = s[0]
for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        c += s[i]
        m = max(m, c, key=len)
    else:
        c = ''

print(m)
