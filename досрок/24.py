# -*- coding: utf-8 -*-

# from itertools import product
#
# # 1 cпособ
# s = open('24__1kuxq.txt').readline()
# pairs = [''.join(i) for i in list(product('QSR', repeat=2))]
# for j in range(2):
#     for i in pairs:
#         s = s.replace(i, f'{i[0]} {i[1]}')
# print(max(len(i) for i in s.split()))
#
# # 2 способ
# c = m = 1
# pairs = [''.join(i) for i in list(product('QSR', repeat=2))]
# for i in range(len(s) - 1):
#     if s[i] + s[i + 1] not in pairs:
#         c += 1
#         m = max(c, m)
#     else:
#         c = 1
#
# print(m)
s = open('24__1as9p.txt').readline()
s = s.replace('B', 'C')
s = s.replace('ACC', '*')
s = s.replace('A', ' ').replace('C', ' ')
print(max([len(i) for i in s.split()]) * 3)