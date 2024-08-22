o,i = input().split()
if o == "E":
    out = ''
    count = 0
    oc = ''
    for c in i:
        if oc == '':
            oc = c
            count = 1
        elif c != oc:
            out += oc + str(count)
            oc = c
            count = 1
        else:
            count += 1
    out += oc + str(count)
    print(out)
else:
    out = ''
    for j in range(0, len(i), 2):
        out += i[j] * int(i[j+1])
    print(out)
