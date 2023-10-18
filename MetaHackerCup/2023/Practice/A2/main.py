from pathlib import Path
from typing import List

lines = Path("input.txt").read_text().splitlines()
out: List[str] = []

def process(a: int, b: int, c: int) -> int:
    if c < a and c < b:
        return 0
    if b <= a:
        return (c // b)*2 - 1
    if (2*a) <= b:
        return (c // a)
    if c < b:
        return (c // a)

    max_value = 0
    for d in range(c//b, -1, -1):
        s = (c - (d*b)) // a
        k = min(s+d*2, s*2+d*2-1)
        if k > max_value:
            max_value = k
        else:
            break
    
    return max_value

for i, line in enumerate(lines[1:], start=1):
    args = map(int, line.split())
    out.append(f"Case #{i}: {process(*args)}")

Path("output.txt").write_text('\n'.join(out))
