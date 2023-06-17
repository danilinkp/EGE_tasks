c = 0
for i in range(11, 10 ** 9, 11):
    s = str(i)
    if len(s) > 5:
        if s[0] == '1' and s[2:4] == '38' and s[5:7] == '70':
            c += 1

print(c)