for x in range(20, 31):
    s = ''
    n = x
    while n:
        s += str(n % 3)
        n //= 3
    if s[:2] == '11':
        print(x)
