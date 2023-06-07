c = 0
for n in range(1, 2000):
    x5 = x16 = x2 = n
    s5 = s16 = ''
    s2 = bin(x2)[2:]
    while x5:
        s5 += str(x5 % 5)
        x5 //= 5
    while x16:
        if x16 % 16 > 10:
            if x16 % 16 == 10:
                s16 += 'a'
            if x16 % 16 == 11:
                s16 += 'b'
            if x16 % 16 == 12:
                s16 += 'c'
            if x16 % 16 == 13:
                s16 += 'd'
            if x16 % 16 == 14:
                s16 += 'e'
            if x16 % 16 == 15:
                s16 += 'f'
        else:
            s16 += str(x16 % 16)
        x16 //= 16
    if len(s5) <= 4 and len(s2) >= 5 and s16[0] == 'c':
        c += 1

print(c)