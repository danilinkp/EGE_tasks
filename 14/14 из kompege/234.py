n = 2 * 27 ** 7 + 3 ** 10 - 9

s = ''

while n:
    s += str(n % 3)
    n //= 3

print(s.count('0'))
