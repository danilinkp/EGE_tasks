s = open('24_1040.txt').readline()
for i in 'qwertyuiopasdfghjklzxcvbnm':
    s = s.replace(i, ' ')
print(s.split())
print(max([len(i) for i in s.split()]))