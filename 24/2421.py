s = open('24_2421.txt').readline()
s = s.replace('D', ' ')
print(max([len(i) for i in s.split()]))