from sys import setrecursionlimit

setrecursionlimit(10000)


def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return f(n - 1) * n


print(f(2023) / f(2022))
