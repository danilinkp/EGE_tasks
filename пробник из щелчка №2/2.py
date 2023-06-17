print('x z y f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (((x <= (not y)) <= (not z)) == (x and not y)) == 1:
                print(x, z, y, 1)