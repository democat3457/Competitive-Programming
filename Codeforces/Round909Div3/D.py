from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    d = defaultdict(lambda: 0)
    for s in input().split():
        i = int(s)
        x = i
        pow_2 = 0
        while x % 2 == 0:
            pow_2 += 1
            x //= 2
        d[(x, i-pow_2)] += 1
    total = 0
    for c in d.values():
        total += (c * (c-1)) // 2
    print(total)
