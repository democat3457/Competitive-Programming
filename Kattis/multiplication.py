def printjoin(*args):
    print(''.join(args))

while True:
    line = input()
    if line == '0 0':
        break
    num1, num2 = line.split()
    d1, d2 = len(num1), len(num2)
    product = str(int(num1)*int(num2))
    side_product = product[:-d1].rjust(d2)
    bottom_product = product[-d1:]

    print('+--'+'----'*d1+'-+')
    print('| ',*[f' {i} ' for i in num1],' |')
    print('| +'+'---+'*d1+' |')
    prev_exists = False
    for i,j in enumerate(num2):
        products = [str(int(x)*int(j)).rjust(2,'0') for x in num1]
        printjoin('|','/' if prev_exists else ' ','|',*[f'{p[0]} /|' for p in products],' |')
        printjoin('| |',*[f' / |' for _ in products],j,'|')
        printjoin('|',side_product[i],'|',*[f'/ {p[1]}|' for p in products],' |')
        print('| +'+'---+'*d1+' |')

        if side_product[i] != ' ':
            prev_exists = True
    printjoin('|','/' if len(product[:-d1]) else ' ','/'.join([f' {p} ' for p in bottom_product]),'   |')
    print('+--'+'----'*d1+'-+')
