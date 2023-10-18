from pathlib import Path
from typing import List

lines = Path("input.txt").read_text().splitlines()
out: List[str] = []

for i, line in enumerate(lines[1:], start=1):
    s,d,k = map(int, line.split())
    buns = s*2+d*2
    patties = s+d*2
    if buns >= k+1 and patties >= k:
        out.append(f"Case #{i}: YES")
    else:
        out.append(f"Case #{i}: NO")

Path("output.txt").write_text('\n'.join(out))
