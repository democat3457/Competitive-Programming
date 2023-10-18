for _ in range(int(input())):
    input()
    s = input()

    def proc(n, c):
        # print("e",n,chr(c))
        if len(n) == 1:
            if ord(n) == c:
                return 0
            return 1
        h = len(n)//2
        left_all  = sum(1 for i in n[:h] if ord(i) != c)
        right_all = sum(1 for i in n[h:] if ord(i) != c)
        return min(left_all+proc(n[h:],c+1),
                   proc(n[:h],c+1)+right_all)

    print(proc(s, ord('a')))