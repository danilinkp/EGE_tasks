s = open('24_21.txt').readline()
s = s.replace('XX', 'X X').replace('YY', 'Y Y').replace('ZZ', 'Z Z')
s = s.replace('XX', 'X X').replace('YY', 'Y Y').replace('ZZ', 'Z Z')
print(max([len(i) for i in s.split()]))
print(max(s.split(), key=len))