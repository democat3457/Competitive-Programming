for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    half = len(a)//2
    a1, a2 = a[:half], a[half:]
    print((a1[-1]-a1[0]) + (a2[-1]-a2[0]))
    for x,y in zip(a1, a2):
        print(x,y)