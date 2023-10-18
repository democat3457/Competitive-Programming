n,s,m = tuple(map(int,input().split()))
arr = list(map(int, input().split()))
def run(s,m):
    visited_indices = []
    num = 0
    while True:
        if arr[s] == m:
            return 'magic', num
        if s in visited_indices:
            return 'cycle', num
        visited_indices.append(s)
        s = arr[s] + s
        num += 1
        if s >= len(arr):
            return 'right', num
        if s < 0:
            return 'left', num

st, num = run(s-1,m)
print(st)
print(num)
