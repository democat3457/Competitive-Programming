# wrong answer

from collections import defaultdict

"""
4
4
2 3 4 4
4
2 3 12 18
5
2 3 5 12 18
6
2 3 12 12 18 18

"""

for _ in range(int(input())):
    size = int(input())
    count = defaultdict(int)
    for i in map(int, input().split()):
        count[i] += 1
    uniq = sorted(count.keys())
    good = (size * (size-1)) // 2
    # print(good, count)
    bad = 0
    dontcheck = set()
    base_nums = []
    for u in uniq:
        # within itself
        bad += (count[u] * (count[u]-1)) // 2
        if u in dontcheck:
            continue
        base_nums.append(count[u])
        # with others divisible
        divs = [m for m in uniq if m % u == 0]
        filtered_divs = [d for d in divs if d not in dontcheck]
        separate_div_sum = sum(count[m] for m in divs if m in dontcheck)
        dontcheck.update(divs)
        amnts = [count[m] for m in filtered_divs]
        t = sum(amnts)
        bad += separate_div_sum * t
        while len(amnts):
            a = amnts.pop()
            t -= a
            bad += a * t
    really_good = 0
    # base_nums is coprimes
    # t = sum(base_nums)
    # while len(base_nums):
    #     a = base_nums.pop()
    #     t -= a
    #     really_good += a * t
    # print(good, bad, really_good)
    print(good-bad+really_good)
