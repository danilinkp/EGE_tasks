from math import tan, degrees


def f(n):
    if n < 12:
        return n + int(tan(n))
    if n >= 12 and n % 6 == 0:
        return f(n // 2) + 1
    if n > 12 and n % 6 != 0:
        return f(n - 3) + 3


for n in range(10000):
    if f(n) == 17:
        print(n)
        break
