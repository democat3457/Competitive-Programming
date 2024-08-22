import math
p,q,s = map(int, input().split())
print("yes" if math.lcm(p,q) <= s else "no")