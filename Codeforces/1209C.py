'''
11
6
258285
4
6967
5
12312
6
129278
5
36792
12
040425524644
1
0
9
123456789
2
98
3
987
6
611444

'''

def process(ds: list[int]):
    less = set()
    greater = set()
    if len(ds) == 1:
        return 1
    uniq = set(ds)
    if len(uniq) == 1:
        return '1' * len(ds)
    if len(uniq) == 2:
        a, b = min(uniq), max(uniq)
        return ''.join(('1' if d == a else '2') for d in ds)
    first_ineq = -1,0,0,0
    last_ineq = len(ds),0,0
    for e,(j,i) in enumerate(zip(ds, ds[1:])):
        if j > i:
            if first_ineq[0] == -1:
                first_ineq = e,i+1,j,i+1
            if i not in less:
                if len(less) > 0 and i < max(less):
                    return '-'
                less.add(i)
            if j not in greater:
                if len(greater) > 0 and j < max(greater):
                    return '-'
                greater.add(j)
            last_ineq = e,i,j
    if first_ineq[0] >= 0:
        for i in ds[:first_ineq[0]]:
            if i > first_ineq[2]:
                return '-'
            elif i >= first_ineq[3]:
                greater.add(i)
                first_ineq = first_ineq[0], first_ineq[1], first_ineq[2], i
            elif i >= first_ineq[1]:
                return '-'
    for i in ds[last_ineq[0]+2:]:
        if i < last_ineq[1]:
            return '-'
        elif i < last_ineq[2]:
            less.add(i)
            last_ineq = last_ineq[0], i, last_ineq[2]
    if not len(less) and not len(greater):
        return '1' * len(ds)
    if max(less) > min(greater):
        return '-'
    less_l = [ (l, False) for l in sorted(less) ]
    greater_l = [ (g, False) for g in sorted(greater) ]
    result_1 = less.copy()
    result_2 = greater.copy()
    s = ''
    for i in ds:
        # print(s, less, greater)
        if i < min(less) and not less_l[0][1]:
            s += '1'
            result_1.add(i)
            less_l.insert(0, (i, True))
            less.add(i)
            print('x')
            continue
        if less_l[0][1] and i >= max(less) and i < min(greater) and not greater_l[0][1]:
            s += '2'
            result_2.add(i)
            greater_l.insert(0, (i, True))
            greater.add(i)
            continue

        if i in greater:
            if i == greater_l[0][0]:
                s += '2'
                greater_l[0] = (i, True)
                continue
            elif i == greater_l[1][0] and greater_l[0][1]:
                s += '2'
                greater_l[1] = (i, True)
                greater.remove(greater_l[0][0])
                del greater_l[0]
                continue
        if i in less:
            if i == less_l[0][0]:
                s += '1'
                less_l[0] = (i, True)
                continue
            elif i == less_l[1][0] and less_l[0][1]:
                s += '1'
                less_l[1] = (i, True)
                less.remove(less_l[0][0])
                del less_l[0]
                continue

        if greater_l[0][1] and greater_l[0][0] < i and (len(greater_l) > 1 and i < greater_l[1][0]):
            s += '2'
            result_2.add(i)
            greater.remove(greater_l[0][0])
            greater.add(i)
            greater_l[0] = (i, True)
        elif less_l[0][1] and less_l[0][0] < i and (len(less_l) > 1 and i < less_l[1][0]):
            s += '1'
            result_1.add(i)
            less.remove(less_l[0][0])
            less.add(i)
            print('r')
            less_l[0] = (i, True)
        elif greater_l[0][1] and greater_l[0][0] < i and (len(greater_l) == 1):
            s += '2'
            result_2.add(i)
            greater.remove(greater_l[0][0])
            greater.add(i)
            greater_l[0] = (i, True)
        elif less_l[0][1] and less_l[0][0] < i and (len(less_l) == 1):
            s += '1'
            print('t')
            result_1.add(i)
            less.remove(less_l[0][0])
            less.add(i)
            less_l[0] = (i, True)
        else:
            return '-'

        if max(result_1) > min(result_2):
            return '-'
    return s

n = int(input())
for i in range(n):
    input()
    inp = input()
    ds = list(map(int, inp))
    # if n == 10000 and i == 1286:
    #     print(inp)
    print(process(ds))