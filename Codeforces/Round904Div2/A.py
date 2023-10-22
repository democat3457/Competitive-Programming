for _ in range(int(input())):
    x,k = map(int, input().split())
    while True:
        if sum(int(i) for i in str(x)) % k == 0:
            print(x)
            break
        x += 1