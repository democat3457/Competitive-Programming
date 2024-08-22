def solve(s: str):
    if len(s) < 4:
        return False
    if s.startswith('2020'):
        return True
    if s.endswith('2020'):
        return True
    if s.startswith('2') and s.endswith('020'):
        return True
    if s.startswith('20') and s.endswith('20'):
        return True
    if s.startswith('202') and s.endswith('0'):
        return True
    return False

for _ in range(int(input())):
    input()
    s = input()
    print('YES' if solve(s) else 'NO')
