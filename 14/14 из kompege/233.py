n = 3 * 16 ** 8 - 4 ** 5 + 3

s = ''

while n:
    s += str(n % 4)
    n //= 4

print(s.count('3'))
