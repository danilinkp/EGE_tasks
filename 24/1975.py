s = open('24_1975.txt').readline()
s = s.replace('PP', 'P P')
s = s.replace('PP', 'P P')
print(len(max(s.split(), key=len)))