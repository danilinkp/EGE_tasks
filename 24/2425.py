s = open('24_2425.txt').readline()
c = ''
while c in s:
    c += 'DBAC'
print(c - 1)