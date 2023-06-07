n = 51 * 7 ** 12 - 7 ** 3 - 22

s = []

while n:
    s.append(n % 7)
    n //= 7

print(sum(s))
