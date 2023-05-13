s = open('24_2251.txt').readline()
s = s.split('D')
m = 0
f = ''
for i in range(len(s) - 2):
    if len(s[i] + 'D' + s[i + 1] + 'D' + s[i + 2]) > m:
        m = len(s[i] + 'D' + s[i + 1] + 'D' + s[i + 2])
print(m)
