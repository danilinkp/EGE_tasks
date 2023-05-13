with open('26__1kuxo.txt', 'r') as f:
    f = [list(map(int, i.split())) for i in f.read().split('\n')]
    count, n = f[0][0], f[0][1]
    numbers = f[1:]
    stock = [0] * count
    k = 0
    was = [-1000000000] *n
    for time in range(1440): # time -> nums
        for start in range(n): # start -> nums -> elem
            if numbers[start][0] == time:
                for index in range(count):
                    if stock[index] == 0:
                        stock[index] = 1
                        was[start] = index
                        k += 1
                        if k == 463:
                            print(index)
                        break
        for finish in range(n):
            if numbers[finish][1] == time and was[finish] >= 0:
                stock[was[finish]] = 0

    print(k)