# -*- coding: utf-8 -*-

from itertools import product

c = 0
for i in product('КЛМНО', repeat=4):
    s = ''.join(i)
    c += 1
    if s[:2] == 'КМ':
        print(s)
        print(c)

