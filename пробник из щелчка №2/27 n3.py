def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


f = open('27 b n3.txt')
n = int(f.readline())
k = [10 ** 20] * n
k_p = 0
c = 0
s = ms = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if is_prime(x):
        k_p += 1
    if k_p % 3 == 0:
        ms = max(s, ms)
    s1 = s - k[k_p % 3]
    ms = max(ms, s1)

    k[k_p] = min(k[k_p], s)

print(ms)
