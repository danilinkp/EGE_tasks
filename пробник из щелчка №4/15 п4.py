from itertools import combinations


def f(x):
    D = 31 <= x <= 54
    K = 43 <= x <= 72
    A = a1 <= x <= a2
    return D <= (((not K) and (not A)) <= K)


Ox = [i / 4 for i in range(31 * 4, 72 * 4 + 1)]
m = []

for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2 - a1)

print(round(min(m)))
