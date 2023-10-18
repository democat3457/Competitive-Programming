n,w,h = map(int, input())
envelopes = {}
for i in range(n):
    wi,hi = map(int, input())
    if wi <= w or hi <= h:
        continue
    if (wi,hi) in envelopes.values():
        continue
    envelopes[i+1] = (wi,hi)


