import sys

c = 0
data = [i.split('\t') for i in map(str.strip, sys.stdin)]
for i in data:
    if len(set(i)) == 5:
        s = sorted([int(j) for j in i])
        if (s[-1] - s[0]) ** 2 < (s[1] + s[2] + s[3]) ** 2:
            c += 1

print(c)

# ����� ������ ����������� ������ � ������ � ��������
# ����� ����������� ����� ������ ctrl + d ��� ��� ��� ��� �� ����� � sys.stdin
