with open(file='Задание_26__d0r7__rjfm.txt') as f:
    s, n = map(int, f.readline().split())
    nums = sorted([int(i) for i in f.readlines()[1:]])
    c = 0
    c_n = 0
    for i in nums:
        if c + i > s:
            break
        else:
            c += i
            c_n += 1
    free = s - (c - nums[c_n - 1])
    print(c_n, free)