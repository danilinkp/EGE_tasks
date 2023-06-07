for x in range(5000):
    n = 4 ** 2015 + 2 ** x - 2 ** 2015 + 15
    s = ''
    while n:
        s += str(n % 2)
        n //= 2
    if s.count('1') == 500:
        print(x)
        break
