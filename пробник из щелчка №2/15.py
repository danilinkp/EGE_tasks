from itertools import combinations


def f(x):
    P = 19 <= x <= 56
    Q = 32 <= x <= 84
    A = a1 <= x <= a2
    return (not (A and Q)) <= (P)


Ox = [i / 4 for i in range(19 * 4, 84 * 4 + 1)]
m = []

for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2 - a1)

print(round(min(m)))
