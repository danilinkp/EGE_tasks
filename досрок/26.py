# with open('26__1kuxo.txt', 'r') as f:
#     f = [list(map(int, i.split())) for i in f.read().split('\n')]
#     count, n = f[0][0], f[0][1]
#     numbers = f[1:]
#     stock = [0] * count
#     k = 0
#     was = [-1000000000] * n
#     for time in range(1440):  # time -> nums
#         for start in range(n):  # start -> nums -> elem
#             if numbers[start][0] == time:
#                 for index in range(count):
#                     if stock[index] == 0:
#                         stock[index] = 1
#                         was[start] = index
#                         k += 1
#                         if k == 463:
#                             print(index)
#                         break
#         for finish in range(n):
#             if numbers[finish][1] == time and was[finish] >= 0:
#                 stock[was[finish]] = 0
#
#     print(k)

f = open('26__1kuxo.txt')
k, n = map(int, f.readline().split())
a = []
for i in range(n):
    p, u = [int(s) for s in f.readline().split()]
    a.append((p, u))
a.sort()
d = [0] * k  # ячейки
m = 0
ans = 0
for i in range(n):
    p, u = a[i]
    for cell in range(k):
        if p > d[cell]:
            ans += 1
            d[cell] = u
            m = cell + 1
            break
print(ans, m)
