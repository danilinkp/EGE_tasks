s = open('24_2250.txt').readline()
s = s.split('A')
m = 0
f = ''
for i in range(len(s) - 1):
    if len(s[i] + s[i + 1]) > m:
        m = len(s[i] + s[i + 1])
        f = s[i] + s[i + 1]
print(m, f)
