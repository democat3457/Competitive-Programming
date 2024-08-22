"""
1 1 1 1 -> YES
2 2 0 1 -> NO
2 1 2 1 -> NO
2 1 0 1 -> YES
1 2 0 1 -> YES
1 3 0 1 -> NO
1 3 0 2 -> YES
"""

def process(s: int, o: int, k: int):
    if k > s or k > o:
        return True
    if k < s and k < o:
        return False
    

w,s,c,k = map(int, input().split())
o = w + c
print('YES' if process(s, o, k) else 'NO')