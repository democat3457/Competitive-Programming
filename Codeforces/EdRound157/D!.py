target = int(input())
ints = list(map(int, input().split()))
for to_try in range(target):
    seen = list()
    seen.append(to_try)
    a = to_try
    for i in ints:
        a = i ^ a
        if a in seen:
            break
        if a >= target:
            break
        seen.append(a)
    else:
        print(' '.join(map(str, seen)))
        break