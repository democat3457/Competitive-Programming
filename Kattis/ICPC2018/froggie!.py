def run():
    ln,w = map(int, input().split())
    lanes = [ tuple(map(int, input().split())) for i in range(ln) ]
    start, dirs = input().split()
    start = int(start)
    pos = [start, ln]
    pos[0]

print("safe" if run() else "squish")
