s = open('24_1146.txt').readline()
s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ').replace('E', ' ').replace('F', ' ')
print(min([len(i) for i in s.split()]) + 2)
