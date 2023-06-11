with open(file='26_2615.txt') as f:
    n = int(f.readline())
    nums = sorted([int(i) for i in f.readlines()])
    for i in range(n):
        if sum(nums[:i]) < nums[i]:
            print(sum(nums[:i]), nums[i])