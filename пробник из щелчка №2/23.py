s = set()


def f(c, st):
    global s
    if st > 12:
        return 0
    if st == 12:
        s.add(c)
    if st < 12:
        f(c + 2, st + 1)
        f(c * 2 + 1, st + 1)


f(6, 0)
print(len(s))
