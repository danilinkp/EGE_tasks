def f(a, b, m):
    if a + b >= 52:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 1, b, m - 1), f(a * 3, b, m - 1), f(a, b + 1, m - 1), f(a, b * 3, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else any(h)


print('19)', [s for s in range(1, 46) if not f(5, s, 1) and f(5, s, 2)])  # all -> any in else
# print('20)', [s for s in range(1, 78) if not(f(s, 1)) and f(s, 3)])
# print('21)', [s for s in range(1, 78) if not(f(s, 2)) and f(s, 4)])
