# time limit

for _ in range(int(input())):
    n = int(input())
    s = list(reversed(input()))
    if s == '0':
        print(0)
        break

    ns = s.count('1')
    zero_indices = [i for i,x in enumerate(s) if x == '0']
    one_indices = []
    out = []
    # running = ''
    all_zeroes = True
    for i in range(1, n+1):
        # i counts how many zeroes need to be rjusted
        if i > (n-ns):
            out.append('-1')
            continue
        
        all_zeroes = all_zeroes and s[i-1] == '0'
        # running += s[i-1]
        if s[i-1] == '1':
            one_indices.append(i-1)
        else:
            zero_indices.remove(i-1)
        if all_zeroes:
            out.append('0')
            continue
        total = 0
        tempzero = zero_indices.copy()
        for x in one_indices:
            total += tempzero.pop(0) - x
        out.append(str(total))
    
    print(' '.join(out))


