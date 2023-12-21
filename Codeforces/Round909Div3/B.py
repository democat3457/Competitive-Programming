import math

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1 or all(a == arr[0] for a in arr):
        print(0)
    else:
        max_diff = 0
        for i in range(1, math.ceil(math.sqrt(n))):
            if n % i != 0:
                continue
            for k in (i, n // i):
                min_weight = 10**9
                max_weight = 0
                for j in range(n//k):
                    sl = slice(j*k, (j+1)*k)
                    weight = sum(arr[sl])
                    if weight > max_weight:
                        max_weight = weight
                    if weight < min_weight:
                        min_weight = weight
                diff = max_weight - min_weight
                if diff > max_diff:
                    max_diff = diff
        print(max_diff)
