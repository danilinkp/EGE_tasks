for x in '0123456789abcdefg':
    if (int(f'9759{x}', 17) + int(f'3{x}108', 17)) % 11 == 0:
        print((int(f'9759{x}', 17) + int(f'3{x}108', 17)) / 11)