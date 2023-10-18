from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    counts = defaultdict(int)
    c = 0
    for i in range(n):
        c += sum(v for l,v in counts.items() if a[i] <= l)
        counts[a[i]] += 1
    print(c)