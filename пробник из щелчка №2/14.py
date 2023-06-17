for x in '0123':
    if (int(f'20{x}3', 4) + int(f'1{x}32', 4)) % 3 == 0:
        print((int(f'20{x}3', 4) + int(f'1{x}32', 4)) / 3)
        print(x)