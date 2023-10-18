import sys
import math

from tqdm import tqdm

def input():
    return "?" * 500000

MOD = 10**9 + 7

string = input().strip().lstrip("0").rstrip("1")
if len(string) <= 1:
    print(0)
    sys.exit(0)

ones = string.count('1')
num_of_questions = string.count('?')

normal_dists = 0
total_distance = 0
for i in range(len(string)):
    dist = len(string)-1 - i
    if string[i] == '?':
        total_distance += dist
    elif string[i] == '1':
        normal_dists += dist

total_inv_from_qs = total_distance * (2**(num_of_questions-1))
total_inv = total_inv_from_qs + (normal_dists * (2**num_of_questions))

for n in tqdm(range(num_of_questions+1), mininterval=1):
    total_num_ones = ones + n
    amnt_to_remove = int(total_num_ones * (total_num_ones-1) / 2)
    if amnt_to_remove == 0:
        continue
    total_inv -= amnt_to_remove * math.comb(num_of_questions, n)

print(int(total_inv) % MOD)
