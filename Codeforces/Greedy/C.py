for _ in range(int(input())):
    a = input()
    b = input()
    prev_0 = False
    for i,j in zip(a,b):
        if i == j == '0':
            prev_0 = True
            continue
        if prev_0 and i == j == '1':
            print('YES')
            break
        prev_0 = False
    else:
        print('NO')