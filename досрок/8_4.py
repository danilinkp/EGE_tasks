# -*- coding: utf-8 -*-

from itertools import product

odd = [''.join(i) for i in product('0246', repeat=2)]
nodd = [''.join(i) for i in product('135', repeat=2)]

c = 0
for i in product('0123456', repeat=6):
    s = ''.join(i)
    if s[0] != '0' and s.count('6') == 1 and not any([i in s for i in odd]) and not any([i in s for i in nodd]):
        print(s)
        c += 1

print(c)
