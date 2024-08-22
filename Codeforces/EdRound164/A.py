import math
for _ in range(int(input())):
    n,m,k = map(int, input().split())
    print('YES' if n-math.ceil(n/m) > k else 'NO')