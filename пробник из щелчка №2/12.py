s = '1' + '0' * 100 + '333'

while '10' in s or '11' in s or '330' in s:
    if '10' in s:
        s = s.replace('10', '1', 1)
    elif '11' in s:
        s = s.replace('11', '3', 1)
    elif '330' in s:
        s = s.replace('330', '100', 1)

print(s)