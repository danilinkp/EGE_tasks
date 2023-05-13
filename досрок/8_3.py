# -*- coding: utf-8 -*-

from itertools import product

c = 0
for i in product('ВОРТА', repeat=6):
    s = ''.join(i)
    c += 1
    if s == 'ВОРОТА':
        print(s)
        print(c)
