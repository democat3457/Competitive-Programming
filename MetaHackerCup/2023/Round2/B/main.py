from pathlib import Path
from typing import List
from collections import defaultdict

lines = Path("input.txt").read_text().splitlines()
# lines = """
# 1
# 6
# 3 2 3 5 6 4
# 4 6 5 3 2 3
# """.strip().splitlines()
out: List[str] = []

in_gen = (line for line in lines)
def input():
    return next(in_gen)

def process(a: List[int], b: List[int], n: int):
    big_arr = a + b + a
    for e,(i,j) in enumerate(zip(big_arr, big_arr[1:-2*n+1])):
        if i == j:
            x = i
            if big_arr[e+n] == big_arr[e+n+1]:
                y = big_arr[e+n]
                start_a = -1
                if x < y:
                    start_a = e+1
                    new_a = big_arr[e+1:e+n+1]
                    new_b = big_arr[e+n+1:e+n+n+1]
                elif x > y:
                    start_a = e+n+1
                    new_a = big_arr[e+n+1:e+n+n+1]
                    new_b = big_arr[e+1:e+n+1]
                if start_a >= 0:
                    if new_a == list(reversed(new_b)):
                        for m in range(n//2):
                            if new_a[m] >= new_b[m]:
                                break
                        else:
                            return start_a % (2*n)
    return -1





for i in range(1, int(input())+1):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f"Processing case {i}...")
    s = f"Case #{i}: {process(a, b, n)}"
    # print(s)
    out.append(s)

Path("output.txt").write_text('\n'.join(out))
