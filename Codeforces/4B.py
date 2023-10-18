d, sumTime = map(int, input().split())
mn, mx = 0,0
ls = []
for i in range(d):
    t = tuple(map(int, input().split()))
    ls.append(t)
    mn += t[0]
    mx += t[1]

if not (mn <= sumTime <= mx):
    print('NO')
else:
    print('YES')
    if mn == sumTime:
        print(' '.join(map(lambda x: str(x[0]), ls)))
    elif mx == sumTime:
        print(' '.join(map(lambda x: str(x[1]), ls)))
    else:
        nums = [x[0] for x in ls]
        remaining = sumTime - mn

        for i in range(len(nums)):
            max_diff = ls[i][1] - ls[i][0]
            if max_diff >= remaining:
                nums[i] += remaining
                break
            else:
                nums[i] += max_diff
                remaining -= max_diff
        
        print(' '.join(map(str, nums)))


