for n in range(20000):
    x6 = x5 = x11 = n
    s6 = s5 = s11 = ''
    while x6:
        s6 += str(x6 % 6)
        x6 //= 6
    while x5:
        s5 += str(x5 % 5)
        x5 //= 5
    while x11:
        s11 += str(x11 % 11)
        x11 //= 11
    s11 = s11.replace('10', 'a')
    if len(s6) == 2 and len(s5) == 3 and s11[::-1][-1] == '1':
        print(n)
