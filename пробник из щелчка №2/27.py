f = open('Задание 27B.txt')
n = int(f.readline())


def neff():
    a = [int(i) for i in f]
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if ((j - i) % 9) == ((a[i] + a[j]) % 9):
                c += 1

    print(c)


def eff():
    a = [int(i) for i in f]
    c = 0
    k = [[0] * 9 for i in range(9)]
    for i in range(n):
        x = a[i]
        for j in range(9):
            dop = (j - x % 9) % 9
            ind = (i - j % 9) % 9
            c += k[ind][dop]
        k[i % 9][x % 9] += 1
    print(c)


# neff()
eff()