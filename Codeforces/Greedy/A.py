for _ in range(int(input())):
    input()
    nums = sorted(map(int, input().split()))
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 1:
            print('NO')
            break
    else:
        print('YES')
