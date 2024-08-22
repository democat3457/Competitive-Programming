input()
s = input()
i = -1
while i < len(s):
    last_r = i
    i += 1
    count = 0
    while i < len(s) and s[i] == "L":
        i += 1
        count += 1
    print(i+1)
    for j in range(i-1, last_r, -1):
        print(j+1)
