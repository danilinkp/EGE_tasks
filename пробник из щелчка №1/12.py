s = '8' * 40 + '2' * 50 + '4' * 40
while '28' in s or '84' in s or '24' in s:
    if '24' in s:
        s = s.replace('24', '42', 1)
    elif '84' in s:
        s = s.replace('84', '48', 1)
    elif '28' in s:
        s = s.replace('28', '82', 1)

print(s)

s =  '8' * 40 + '4' * 40 + '2' * 50
while '28' in s or '84' in s or '24' in s:
    if '24' in s:
        s = s.replace('24', '42', 1)
    elif '84' in s:
        s = s.replace('84', '48', 1)
    elif '28' in s:
        s = s.replace('28', '82', 1)

print(s[24], s[70], s[104])
