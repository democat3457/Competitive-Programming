for _ in range(int(input())):
    x = input()
    y = input()
    x,y = sorted((x,y))
    if x == y:
        print(x)
        print(y)
    else:
        nx = ny = ''
        found = False
        for i in range(len(x)):
            if x[i] == y[i]:
                nx += x[i]
                ny += y[i]
                continue
            if not found:
                found = True
                nx += x[i]
                ny += y[i]
            else:
                b,a = sorted((int(x[i]), int(y[i])))
                nx += str(a)
                ny += str(b)
        print(nx)
        print(ny)
