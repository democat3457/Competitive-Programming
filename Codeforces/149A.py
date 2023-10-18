k = int(input())
total = 0
for i, n in enumerate(sorted(map(int, input().split()), reverse=True)):
    if total >= k:
        print(i)
        quit()
    total += n
if total >= k:
    print(i+1)
else:
    print(-1)