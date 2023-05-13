s = open('24_2419.txt').readline()
s = s.replace('A', ' ').replace('B', ' ')
print(max([len(i) for i in s.split()]))