s = open('24_1145.txt').readline()
s = s.replace('D', ' ')
print(min([len(i) for i in s.split()]) + 2)
