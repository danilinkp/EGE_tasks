def f(x1, x2):
    n1 = (x1 // 100) + (x2 // 100)
    n2 = (x1 // 10 % 10) + (x2 // 10 % 10)
    n3 = (x1 % 10) + (x2 % 10)
    s = sorted([n1, n2, n3])[::-1]
    return int(''.join(list(map(str, s))))


for i in range(1, 1000):
    if f(307, i) == 16118:
        print(i)