input()
potions = 0
positive = 0
# [[total, num], ...]
negative = []
for a in map(int, input().split()):
    if a >= 0:
        potions += 1
        positive += a
    else:
        to_add = []
        for n in negative:
            if (n[0] + a + positive) >= 0:
                # n[0] += a
                # n[1] += 1
                to_add.append([n[0]+a, n[1]+1])
        negative.extend(to_add)
        if (a+positive) >= 0:
            negative.append([a, 1])
print(potions+max(x[1] for x in negative))