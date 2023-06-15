def f(x):
    x_2 = bin(x)[2:]
    if '0' in x_2:
        x_2 = x_2[::-1].replace('0', x_2[:2], 1)
        return int(x_2, 2)


c = 0
for n in range(2, 1000000):
    if f(n) == 255:
        c += 1
print(c)
