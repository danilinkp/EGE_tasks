n = 64 ** 30 + 2 ** 300 - 4

s = ''

while n:
    s += str(n % 8)
    n //= 8

print(s.count('7'))