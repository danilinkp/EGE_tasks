s = open('24_4643.txt').readline()
c = m = 0
pairs = ['11A', '12A', '21A', '22A', '11B', '12B', '21B', '22B']
for j in range(3):
    for i in range(j, len(s) - 2, 3):
        if s[i] + s[i + 1] + s[i + 2] in pairs:
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)