for x in range(5000):
    n = 36 ** 17 - 6 ** x + 71
    s = []
    while n:
        s.append(n % 6)
        n //= 6
    if sum(s) == 61:
        print(x)
        break
