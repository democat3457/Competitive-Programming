from collections import defaultdict

n,m,k = map(int, input().split())
mat = []

conns = defaultdict(set)

for _ in range(n):
    mat.append(input())
for col in zip(*mat):
    cs = set(col)
    for cls in cs:
        conns[cls].update(cs)

groups = 0
while len(conns):
    cls = list(conns.keys())[0]
    visited = set([cls])
    to_visit = set(conns[cls])
    while len(to_visit):
        conn = to_visit.pop()
        if conn in visited:
            continue
        visited.add(conn)
        to_visit.update(conns[conn])
    groups += 1
    for v in visited:
        del conns[v]

print(groups)
