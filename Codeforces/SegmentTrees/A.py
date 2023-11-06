import math

n,m = map(int, input().split())

tree = [0] * (2*n)

for i in range(n):
    tree[n+i] = i+1

for i in range(n-1, 0, -1):
    tree[i] = max(tree[i << 1], tree[i << 1 | 1])

conquered_by = [0] * n

for i in range(m):
    l,r,x = map(int, input().split())
    node = 1
    for j in range(math.ceil(math.log2(n))):
        tree[node]
