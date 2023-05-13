def f(x):
    x_2 = bin(x)[2:]
    if x % 3 == 0:
        x_2 += x_2[-3:]
    else:
        x_2 += bin((x % 3) * 3)[2:]
    return int(x_2, 2)


for n in range(1, 100000):
    if f(n) < 100:
        print(n)
