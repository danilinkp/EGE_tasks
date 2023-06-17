print('y z w x f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= y) or (not (z <= w))) and ((w <= (not x)) or ((not y) <= z))) == 0:
                    print(y, z, w, x, 0)

print([1, 2, 3, 4, 5][1:-1])