with open('26__1ux58.txt', mode='r') as f:
    n = int(f.readline())
    cars = []
    a = [0] * 80
    b = [0] * 20
    for i in range(n):
        p, v, t = f.readline().split()
        cars.append([int(p), int(v) + int(p) - 1, t])
    cars.sort()
    ans = 0
    bs = 0
    no = 0
    for cell in range(80):
        for i in range(n):
            p, u, t = cars[i]
            if t == 'A':
                if p > a[cell]:
                    a[cell] = u
                    ans += 1
                    cars[i] = [0, 0, 'A']
    for cell in range(20):
        for i in range(n):
            p, u, t = cars[i]
            if t == 'B':
                if p > b[cell]:
                    b[cell] = u
                    bs += 1
                    cars[i] = [0, 0, 'B']
            if t == 'A':
                if p > b[cell]:
                    b[cell] = u
                    ans += 1
                    cars[i] = [0, 0, 'A']
print(ans, n - ans - bs)
