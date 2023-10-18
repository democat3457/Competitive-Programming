line = input()
potential = [(i, sum(c < s for s in line[i+1:])) for i, c in enumerate(line)]
total = 0
index = 0
# print(potential)
while len(potential[index+1:]):
    m = max(potential[index+1:], key=lambda x: x[1])
    index = m[0]
    total += 1
print(26-total)