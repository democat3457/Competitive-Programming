input()
ints = list(map(int, input().split()))
even = False
odd = False
for i in ints:
    if i % 2 == 0:
        even = True
    else:
        odd = True

if not (even and odd):
    print(*ints)
else:
    print(*sorted(ints))
