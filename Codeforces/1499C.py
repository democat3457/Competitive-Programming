import math
from operator import itemgetter

def process():
    n = int(input())
    nums: list[int] = []
    even: list[tuple[int, int]] = []
    odd: list[tuple[int, int]] = []
    for i, c in enumerate(map(int, input().split())):
        if i % 2 == 0:
            even.append((i, c))
        else:
            odd.append((i, c))
        nums.append((i, c))
    min_even_absolute = min(even, key=itemgetter(1))
    min_odd_absolute = min(odd, key=itemgetter(1))
    min_even = n, even[0][1], n*even[0][1]
    min_odd = n, odd[0][1], n*odd[0][1]
    since_last_even = n-1, 1, even[0][1]
    since_last_odd = n-1, 1, odd[0][1]
    min_total = min_even[2]+min_odd[2]
    running_total = nums[0][1]+nums[1][1]
    for i, c in nums[2:]:
        # if i > min_even_absolute[0] and i > min_odd_absolute[0]:
        #     break
        recalc_total = False
        running_total += c
        if i % 2 == 0:
            if c > min_even[1]:
                a,b,d = since_last_even
                since_last_even = a-1, b+1, d+c
            else:
                total = min_even[2]
                total_with = since_last_even[2] + c*since_last_even[0]
                if total_with <= total:
                    min_even = since_last_even[0], c, c*since_last_even[0]
                    since_last_even = since_last_even[0], since_last_even[1]+1, c
                    recalc_total = True
        else:
            if c > min_odd[1]:
                a,b,d = since_last_odd
                since_last_odd = a-1, b+1, d+c
            else:
                total = min_odd[2]
                total_with = since_last_odd[2] + c*since_last_odd[0]
                if total_with <= total:
                    min_odd = since_last_odd[0], c, c*since_last_odd[0]
                    since_last_odd = since_last_odd[0], since_last_odd[1]+1, c
                    recalc_total = True
        if recalc_total:
            temp_total = running_total
            temp_total += (n-since_last_even[1]) * min_even[1]
            temp_total += (n-since_last_odd[1]) * min_odd[1]
            if temp_total < min_total:
                # print('set', min_total, temp_total)
                # print(running_total, min_even, min_odd, since_last_even, since_last_odd)
                min_total = temp_total
    return min_total

for _ in range(int(input())):
    print(process())
