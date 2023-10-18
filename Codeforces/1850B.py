for _ in range(int(input())):
    max_b = 0
    max_a = 0
    for i in range(int(input())):
        a,b = map(int, input().split())
        if a <= 10:
            if b > max_b:
                max_b = b
                max_a = i+1
    print(max_a)