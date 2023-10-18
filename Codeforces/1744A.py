n = int(input())
for _ in range(n):
    input()
    table = {}
    arr = list(map(int, input().split()))
    s = input()
    for a,c in zip(arr, s):
        if a not in table:
            table[a] = c
        else:
            if table[a] != c:
                print('NO')
                break
    else:
        print('YES')