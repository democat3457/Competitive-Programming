for _ in range(int(input())):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    all_b = 0
    for x in b:
        all_b |= x
    if len(a) % 2 == 0:
        highest = 0
        lowest = 0
        for x in a:
            highest ^= x
            lowest ^= x | all_b
    else:
        lowest = 0
        highest = 0
        for x in a:
            lowest ^= x
            highest ^= x | all_b

    print(lowest, highest)
        
    