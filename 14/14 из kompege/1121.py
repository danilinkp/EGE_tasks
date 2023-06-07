for x in range(5000):
    n = 4 ** 1014 - 2 ** x + 12
    s = ''
    while n:
        s += str(n % 2)
        n //= 2
    if s.count('0') == 2000:
        print(x)
        break
