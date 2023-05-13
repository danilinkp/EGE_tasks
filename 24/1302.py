s = open('24_1302.txt').readline()
s = s.replace('XZZY', 'XZZ ZZY')
print(max([len(i) for i in s.split()]))