import math

for _ in range(int(input())):
    n,m,d = map(int, input().split())
    s = list(map(int, input().split())) + [n+1]

    min_diff = 0
    min_amt = 0
    if s[0] != 1:
        s = [1] + s
    else:
        min_amt = 1

    for i,j,k in zip(s, s[1:], s[2:]):
        # test removing j
        with_j = int(math.ceil((j-i)/d) + math.ceil((k-j)/d))
        without_j = int(math.ceil((k-i)/d))
        diff = without_j - with_j
        if diff < min_diff:
            min_diff = diff
            min_amt = 1
        elif diff == min_diff:
            min_amt += 1
    
    total = 0
    for i,j in zip(s, s[1:]):
        # sum i (inc) to j (exc)
        total += int(math.ceil((j-i)/d))
    
    print(total+min_diff, min_amt)
