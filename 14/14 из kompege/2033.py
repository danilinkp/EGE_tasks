n = 6 * 144 ** 26 + 11 * 12 ** 75 - 48

s = ''
while n:
    s += str(n % 12)
    n //= 12

print(s.count('11'))