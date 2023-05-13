for x in '123456789abcdef':
    n = int(f'123{x}5', 15) + int(f'1{x}233', 15)
    if n % 14 == 0:
        print(x, n / 14)
        break
