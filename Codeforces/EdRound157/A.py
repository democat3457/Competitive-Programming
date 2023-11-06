for _ in range(int(input())):
    x,y,k = map(int, input().split())
    if x >= y:
        print(x)
        continue
    if (x+k) >= y:
        print(y)
        continue
    print((x+k) + (y-(x+k))*2)