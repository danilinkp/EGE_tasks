# s = open('Задание 24.txt').readline()
# s = s.replace('XXYZ', 'XXY Z')
# print(max([len(i) for i in s.split()]))

s = open('Задание 24 yjvth 3.txt').readline()
s = s.replace('E', 'A').replace('A', ' ')
print(max([len(i) for i in s.split()]))