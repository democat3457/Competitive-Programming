from pathlib import Path
from typing import List

lines = Path("input.txt").read_text().splitlines()
out: List[str] = []

def process(r:int, c:int, a:int, b:int) -> bool:
    return r > c

for i, line in enumerate(lines[1:], start=1):
    args = map(int, line.split())
    out.append(f"Case #{i}: {'YES' if process(*args) else 'NO'}")

Path("output.txt").write_text('\n'.join(out))
