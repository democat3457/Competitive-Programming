from pathlib import Path
from typing import List

lines = Path("input.txt").read_text().splitlines()
out: List[str] = []

in_gen = (line for line in lines)
def input():
    return next(in_gen)

def process(arr: List[str], r: int, c: int):
    visited = []
    for i in range(r):
        for j in range(c):
            if (i,j) in visited:
                continue
            if arr[i][j] == 'W':
                visited.append((i,j))

                empty = set()
                to_visit = [(i,j+1), (i,j-1), (i+1,j), (i-1,j)]
                while len(to_visit):
                    node = to_visit.pop()
                    node_0, node_1 = node
                    if node_0 >= r or node_0 < 0:
                        continue
                    if node_1 >= c or node_1 < 0:
                        continue
                    if node in visited:
                        continue
                    ch = arr[node_0][node_1]
                    if ch == '.':
                        empty.add(node)
                        continue
                    if ch == 'W':
                        visited.append(node)
                        to_visit.extend([(node_0,node_1+1), (node_0,node_1-1), (node_0+1,node_1), (node_0-1,node_1)])
                        continue
                if len(empty) < 2:
                    return True
    return False


for i in range(1, int(input())+1):
    r,c = map(int, input().split())
    arr = []
    for row in range(r):
        arr.append(input())
    out.append(f"Case #{i}: {'YES' if process(arr, r, c) else 'NO'}")

Path("output.txt").write_text('\n'.join(out))
