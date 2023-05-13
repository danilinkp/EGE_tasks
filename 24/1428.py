s = open('24_1428.txt').readline()
s = s.replace('XZ', 'X Z').replace('XY', 'X Y')
print(s.split())
print(max([len(i) for i in s.split()]))