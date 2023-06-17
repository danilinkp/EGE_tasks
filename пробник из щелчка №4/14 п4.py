for x in '0123456789abcdef':
    if (int(f'1587{x}99', 16) + int(f'1{x}048', 16)) % 13 == 0:
        print((int(f'1587{x}99', 16) + int(f'1{x}048', 16)) / 13)
        print(x)