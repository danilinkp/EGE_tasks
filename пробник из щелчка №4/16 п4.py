def f(n):
    if n < 20:
        return n ** 2
    if n > 19 and n % 2 == 0:
        return g(n // 2) * 3 - f(n - 2)
    if n > 19 and n % 2 == 1:
        return g(n - 2)


def g(n):
    if n < 20 and n % 5 != 0:
        return 3 * n + f(n - 2)
    if n < 20 and n % 5 == 0:
        return g(n - 2) + f(n // 5)
    else:
        return n ** 3


for i in range(1, 481):
    if f(i) > 0:
        if sum(map(int, list(str(f(i))))) == 48:
            print(i)
    else:
        if sum(map(int, list(str(f(i))[1:]))) == 48:
            print(i)