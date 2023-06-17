from itertools import product

c = []
word = 'РСКЫНИ'
for i in product(word, repeat=6):
    s = ''.join(i)
    c.append(s)
print(c.index('СЫРНИК') - c.index('СЫРСЫР') - 1)
