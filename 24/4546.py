s = open('24_4546.txt').readline()
# s = s.replace('AAA', '8').replace('ABA', '8').replace('ACA', '8').replace('CAC', '8').replace('CBC', '8').replace('CCC', '8')
# s = s.replace('B', ' ').replace('C', ' ').replace('A', ' ')
#
# print(max(len(i) for i in s.split()))
c = m = 0
pairs = ['AAA', 'ABA', 'ACA', 'CAC', 'CBC', 'CCC']
for j in range(3):
    for i in range(j, len(s) - 2, 3):
        if s[i] + s[i + 1] + s[i + 2] in pairs:
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)
