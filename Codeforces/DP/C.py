import functools
import math
import operator
import sys
sys.setrecursionlimit(int(1e9))

MOD = 1000000007
balls = [ int(input()) for _ in range(int(input())) ]

@functools.cache
def dp(ball_counts: tuple[int, ...], min_color: int):
    if min_color == 0:
        cnt = sum(ball_counts)
        if cnt == 0:
            return 1
        return math.factorial(cnt) // functools.reduce(operator.mul, map(math.factorial, ball_counts), 1)
    total = 0
    for i in range(min_color-1, len(ball_counts)):
        if ball_counts[i] > 0:
            total += dp(ball_counts[:i] + (ball_counts[i] - 1,) + ball_counts[i+1:], min(min_color, i))
            total %= MOD
    return total

print(dp(tuple(balls), len(balls)))
