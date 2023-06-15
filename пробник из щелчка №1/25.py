c = 0
for i in range(0, 10 ** 9, 31):
    s = str(i)
    if s[-3:-1] == '17' and s[-7:-4] == '829':
        c += 1
        print(s)

print(c)