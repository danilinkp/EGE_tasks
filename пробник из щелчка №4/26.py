with open('Задание 26.txt') as f:
    k, n = map(int, f.readline().split())
    mesta = []
    speci = []
    for i in range(k):
        mesta.append(int(f.readline()))
    for i in range(n):
        speci.append(list(map(int, f.readline().split())))
    speci.sort(reverse=True)
    sr = []
    for i in range(k):
        s = 0
        m = 0
        for c in speci:
            if c[1] == i:
                s += c[0]
                m += 1
                if m == mesta[i]:
                    break

        if m > 0:
            sr.append([s / m, i])
    print(sorted(sr)[-1][0], max([i[0] for i in speci if i[1] == 48]))
