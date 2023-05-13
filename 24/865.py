s = open('24_865.txt').readline()
s = s.replace('C', ' ').replace('F', ' ')
print(max([len(i) for i in s.split()]))