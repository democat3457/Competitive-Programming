def convertTo10(s, lang):
    base = len(lang)
    total = 0
    for i, c in enumerate(reversed(s)):
        num = lang.index(c)
        total += num * base**(i)
    return int(total)

def convertFrom10(num, lang):
    base = len(lang)
    if num == 0:
        return lang[0]
    
    s = ''
    
    while num > 0:
        s += lang[int(num % base)]
        num //= base

    return ''.join(reversed(s))

for case in range(int(input())):
    number, source, target = input().split()
    s = convertTo10(number, source)
    print(f"Case #{case+1}:", convertFrom10(s, target))
