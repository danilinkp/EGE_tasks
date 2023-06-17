with open('Задание 26 n3.txt', mode='r') as f:
    n = int(f.readline())
    k = [int(x) for x in f]
    k.sort(reverse=True)
    c = [k[0]]
    for i in range(1, n):
        if c[-1] - k[i] >= 3:
            c.append(k[i])

    print(c)
    print(len(c))
    print(c[-1])
