# -*- coding: utf-8 -*-

from itertools import product

c = 0
for i in product('АВЛОР', repeat=4):
    s = ''.join(i)
    c += 1
    if s[0] == 'Л':
        print(s)
        print(c)
