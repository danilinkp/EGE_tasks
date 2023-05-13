n = [int(i) for i in open('17__1kuxj.txt')]
max_2 = max([i for i in n if len(str(i)) == 2 and i % 10 == 3])
m = []

for i in range(len(n) - 1):
    if len(str(n[i])) == 2 or len(str(n[i + 1])) == 2:
        if (n[i] + n[i + 1]) % max_2 == 0:
            m.append(n[i] + n[i + 1])
print(m, len(m))
