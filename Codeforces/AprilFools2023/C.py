pi = '3141592653589793238462643383279502884197169399'
for i in range(int(input())):
    prod = 1
    for _ in range(int(pi[i])):
        prod *= int(input())
    print(prod)