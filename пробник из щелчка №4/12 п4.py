s = '*' + '2' * 100 + '5' * 10 + '9' * 60
while '*2' in s or '*5' in s or '*9' in s:
    if '*2' in s:
        s = s.replace('*2', '*', 1)
    if '*5' in s:
        s = s.replace('*5', '6*', 1)
    if '*9' in s:
        s = s.replace('*9', '7*', 1)

print(sum(map(int, s[:-1])))
