s = open('24_2426.txt').readline()
s = s.replace('C', ' ').replace('A', ' ').replace('B', ' ')
print(max([len(i) for i in s.split()]))