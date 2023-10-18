import math

def add_digits(num):
    total = 0
    for c in str(num):
        total += int(c)**2
    return total

def is_happy(num):
    visited = []
    while num != 1:
        if num in visited:
            return False
        visited.append(num)
        num = add_digits(num)
    return True

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

n = int(input())
for _ in range(n):
    line = input().split()
    K, num = line
    num = int(num)
    result = is_happy(num) and is_prime(num)
    
    
    if result:
        print(K, num, 'YES')
    else:
        print(K, num, 'NO')
    
    