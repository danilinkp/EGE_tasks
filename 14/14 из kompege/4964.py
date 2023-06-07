for x in '0123456789abcdefghijk':
    for y in '0123456789abcdefghijk':
        if (int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)) % 18 == 0:
            print((int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)) / 18)
            print(x, y)
