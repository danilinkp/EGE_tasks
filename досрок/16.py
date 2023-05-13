def f(n):
    if n >= 2024:
        return n
    else:
        return f(n + 2) + n


print(f(2023) - f(2022))
