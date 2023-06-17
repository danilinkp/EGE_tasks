for i in range(0, 10000000000, 434343):
    s = str(i)

    if len(s) == 8 and s[-2] == '1' and s[3] == '1':
        print(i / 434343)