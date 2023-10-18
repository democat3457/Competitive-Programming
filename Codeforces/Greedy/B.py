import math
n,m = map(int, input().split())
puzzles = sorted(map(int, input().split()))
min_diff = math.inf
for i in range(m-n+1):
    min_diff = min(min_diff, puzzles[i+n-1]-puzzles[i])
print(min_diff)