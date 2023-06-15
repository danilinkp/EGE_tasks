from itertools import combinations


def f(x):
    P = 10 <= x <= 50
    Q = 30 <= x <= 65
    A = a1 <= x <= a2
    return (not A) <= ((P and Q) <= A)


Ox = [i / 4 for i in range(9 * 4, 67 * 4 + 1)]
m = []

for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2 - a1)

print(round(min(m)))
