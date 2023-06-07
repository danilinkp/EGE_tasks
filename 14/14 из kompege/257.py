for n in range(20000):
    x6 = x7 = x13 = n
    s6 = s7 = s13 = ''
    while x6:
        s6 += str(x6 % 6)
        x6 //= 6
    while x7:
        s7 += str(x7 % 7)
        x7 //= 7
    while x13:
        if x13 % 13 > 10:
            if x13 % 13 == 10:
                s13 += 'a'
            if x13 % 13 == 11:
                s13 += 'b'
            if x13 % 13 == 12:
                s13 += 'c'
        else:
            s13 += str(x13 % 13)
        x13 //= 13

    if len(s6) == 3 and len(s7) == 2 and s13[0] == '3':

        print(n)
