n = int(input())
found = {}
for _ in range(n):
    s = input()
    if s not in found:
        print('OK')
        found[s] = 1
    else:
        print(s+str(found[s]))
        found[s] += 1
