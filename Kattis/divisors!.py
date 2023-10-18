import sys
import math
from itertools import chain
from collections import defaultdict
S = sys.stdin.read()

factors = dict()

for num in range(2, 431+1):
    mul = defaultdict(lambda:0)
    item = num
    i = 2
    while i**2 <= item:
        while item % i == 0:
            mul[i] += 1
            item /= i
        i += 1
    if item > 1:
        mul[item] += 1
    factors[num] = mul
    

for line in S.splitlines():
    n, k = tuple(map(int, line.split()))
    mul = defaultdict(lambda:0)

    for item in range(2, n+1):
        for i, j in factors[item].items():
            mul[i] += j

    for item in chain(range(2, k+1), range(2, n-k+1)):
        for i, j in factors[item].items():
            mul[i] -= j

    total = 1
    for v in mul.values():
        total *= v+1
    print(total)
