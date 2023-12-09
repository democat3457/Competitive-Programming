def extrapolate(n, seq):
    if not any(seq):
        return -1,0
    nl = [j-i for i, j in zip(seq, seq[1:])]
    p,q = extrapolate(n, nl)
    return p+1, seq[-1] + q

print(*extrapolate(0, list(map(int, input().split()))[1:]))
