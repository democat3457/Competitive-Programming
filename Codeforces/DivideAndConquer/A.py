for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))

    d = {}
    def proc(n: list, r):
        if len(n) == 1:
            d[n[0]] = r
            return
        max_val = max(n)
        max_index = n.index(max_val)
        d[max_val] = r
        if max_index > 0:
            proc(n[:max_index], r+1)
        if max_index < (len(n)-1):
            proc(n[max_index+1:], r+1)
    
    proc(a, 0)
    print(*[d[i] for i in a])