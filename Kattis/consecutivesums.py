import math

n = int(input())
for _ in range(n):
    num = int(input())

    # 0 + 1, but 0 is not positive
    if num == 1:
        print('IMPOSSIBLE')
        continue
    
    if num % 2 == 1:
        print(f'{num} = {int(math.floor(num/2))} + {int(math.ceil(num/2))}')
        continue
    
    # num is even
    
    # dec = math.sqrt(num*2)
    # if not dec.is_integer():
    #     down, up = math.floor(dec), math.ceil(dec)
    #     if down * up == num * 2:
    #         s = f"{num} = "
    #         s += " + ".join([ str(i) for i in range(1, down+1) ])
    #         print(s)
    #         continue
    
    found = False
    sum = 1+2
    # i is number of terms
    for i in range(3, num // 2 + 1):
        sum += i
        if sum > num:
            break
        add = (num - sum) / i
        if add.is_integer():
            s = f"{num} = "
            s += " + ".join([ str(int(add)+i) for i in range(1, i+1) ])
            print(s)
            found = True
            break

    if not found:
        print('IMPOSSIBLE')
        continue