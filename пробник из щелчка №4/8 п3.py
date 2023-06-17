from itertools import product

w = '01234567'
pairs = []
for i in w:
    pairs.append(f'{i}{i}')
c = 0
for i in product(w, repeat=5):
    s = ''.join(i)
    if s[0] != '0':
        if any([j in s for j in pairs]):
            c += 1
print(c)
