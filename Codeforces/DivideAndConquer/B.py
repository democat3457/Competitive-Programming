for _ in range(int(input())):
    input()
    p = list(map(int, input().split()))

    ops = 0
    def proc(n):
        global ops
        # print("n",n)
        if (max(n) - min(n)+1) != len(n):
            # print("e",max(n),min(n),len(n))
            return -1
        if len(n) == 1:
            return n[0]

        half = len(n)//2
        left = proc(n[:half])
        if left == -1:
            return -1
        right = proc(n[half:])
        if right == -1:
            return -1

        if left > right:
            ops += 1

        return min(n)
    
    if proc(p) == -1:
        print(-1)
    else:
        print(ops)
