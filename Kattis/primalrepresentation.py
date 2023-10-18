import sys
from collections import defaultdict
S = sys.stdin.read()

for line in S.splitlines():
    num = int(line)
    
    neg = num < 0
    num = abs(num)
    
    mul = defaultdict(lambda:0)
    i = 2
    while i**2 <= num:
        while num % i == 0:
            mul[i] += 1
            num //= i
        i += 1
    if num > 1:
        mul[num] += 1
    
    s = "-1 " if neg else ""
    s += " ".join([ str(pair[0]) if pair[1] == 1 else f'{pair[0]}^{pair[1]}' for pair in mul.items() ])
    
    print(s)
