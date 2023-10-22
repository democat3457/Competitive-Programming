from pathlib import Path
from typing import List
from collections import defaultdict

lines = Path("input.txt").read_text().splitlines()
out: List[str] = []

in_gen = (line for line in lines)
def input():
    return next(in_gen)

def process(arr: List[str], r: int, c: int):
    visited = []
    empty_counts = defaultdict(int)
    for i in range(r):
        for j in range(c):
            if (i,j) in visited:
                continue
            if arr[i][j] == 'W':
                visited.append((i,j))

                empty = set()
                group_size = 1
                to_visit = [(i,j+1), (i,j-1), (i+1,j), (i-1,j)]
                while len(to_visit):
                    node = to_visit.pop(0)
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
                        if len(empty) > 1:
                            break
                        continue
                    if ch == 'W':
                        visited.append(node)
                        group_size += 1
                        tv = [(node_0,node_1+1), (node_0,node_1-1), (node_0+1,node_1), (node_0-1,node_1)]
                        for t in tv:
                            if t in visited or t in to_visit:
                                continue
                            to_visit.append(t)
                        continue
                if len(empty) == 1:
                    empty_counts[empty.pop()] += group_size
    return max(empty_counts.values()) if len(empty_counts) else 0


for i in range(1, int(input())+1):
    r,c = map(int, input().split())
    arr = []
    for row in range(r):
        arr.append(input())
    print(f"Processing case {i}...")
    out.append(f"Case #{i}: {process(arr, r, c)}")

Path("output.txt").write_text('\n'.join(out))
