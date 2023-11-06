num_map = {
    1: True,
    15: False,
    6: True,
    20: False,
    25: True,
    21: False,
}
n = int(input())
if n in num_map:
    print('YES'if num_map[n] else'NO')
else:
    print('YES')
