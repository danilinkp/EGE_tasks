def f(x):
    x_2 = bin(x)[2:]
    x_2 += str(int(x_2[-1]) * int(x_2[-2]))
    x_2 += str(int(x_2[0]) * int(x_2[1]))
    return int(x_2, 2)


for n in range(2, 10000):
    if f(n) > 55:
        print(n)
        break
