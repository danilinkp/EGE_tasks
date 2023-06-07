for n in range(3, 11):
    x = 68
    s = ''
    while x:
        s += str(x % n)
        x //= n
    if len(s) == 4 and s[0] == '2':
        print(n)