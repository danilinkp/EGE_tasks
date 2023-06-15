for x in '0123456789abc':
    if (int(f'25{x}3', 13) + int(f'3{x}72', 13)) % 22 == 0:
        print((int(f'25{x}3', 13) + int(f'3{x}72', 13)) / 22)
        print(x)