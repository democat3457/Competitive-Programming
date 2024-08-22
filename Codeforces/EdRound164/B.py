for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    base = nums[0]
    mn = 100000
    cnt = 0
    for n in nums:
        if n == base:
            cnt += 1
        else:
            mn = min(mn, cnt)
            cnt = 0
    mn = min(mn, cnt)
    if mn == len(nums):
        print(-1)
    else:
        print(mn)