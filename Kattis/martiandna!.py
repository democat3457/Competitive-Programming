# Group 1 passed

from collections import defaultdict

def exit(value):
    print(value)
    quit()

n,k,r = map(int, input().split())
dna = []
dna_counts = defaultdict(int)
for _i in input().split():
    i = int(_i)
    dna.append(i)
    dna_counts[i] += 1

requirements = dict()
for _ in range(r):
    b,q = map(int, input().split())
    if dna_counts[b] < q:
        exit('impossible')
    requirements[b] = q

length = sum(requirements.values())
if length > n:
    exit('impossible')

while True:
    for i in range(len(dna)-length+1):
        s = dna[i:i+length]
        for b,q in requirements.items():
            if s.count(b) < q:
                break
        else:
            exit(length)

    length += 1
    if length > len(dna):
        exit('impossible')
