from pathlib import Path
from typing import List
import math

from tqdm import tqdm

lines = Path("input.txt").read_text().splitlines()
out: List[str] = []

def line():
    for l in lines:
        yield l

def process(days: int, apples: List[int]) -> bool:
    if days == 1:
        return apples[0]
    apples.sort()
    last_popped = math.inf
    for i in tqdm(range(len(apples)-1, -1, -1)):
        popped = apples[i]
        if popped == last_popped:
            continue
        last_popped = popped
        filtered = apples.copy()
        filtered.pop(i)
        total = filtered[0] + filtered[days*2-2-1]
        if total == popped:
            continue
        for j in range(1, days-1):
            if total != filtered[j] + filtered[days*2-2-j-1]:
                break
        else:
            return total - popped
    return -1

l = line()
readline = lambda: next(l)

for i in tqdm(range(int(readline()))):
    days = int(readline())
    apples = list(map(int, readline().split()))
    s = f"Case #{i+1}: {process(days, apples)}"
    print(s)
    out.append(s)

Path("output.txt").write_text('\n'.join(out))
