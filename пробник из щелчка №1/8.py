from itertools import product

word = 'ВДЕРЬ'

c = 0
for i in product(word, repeat=7):
    s = ''.join(i)
    c += 1
    if 'В' not in s:
        print(c, s)
        break
