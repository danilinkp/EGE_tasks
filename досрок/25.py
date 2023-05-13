from itertools import product

numbers = '0123456789'
pairs = [''.join(i) for i in list(product(numbers, repeat=2))]
for i in range(10):
    pairs.append(str(i))
pairs.append('')
c = 0
for i in range(10):
    for z in range(10):
        for j in pairs:
            if int(f'12{i}{z}46{j}1') % 273 == 0:
                c += 1

print(c)
