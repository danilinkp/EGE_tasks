for x in range(5000):
    n = 125**200 - 5**x + 74
    s = ''
    while n:
        s += str(n % 5)
        n //= 5
    if s.count('4') == 100:
        print(x)
        break