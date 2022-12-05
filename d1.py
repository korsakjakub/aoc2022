import numpy as np
with open('i1', 'r') as f:
    l = f.readlines()
sums = []
sum = 0
for n in l:
    if n != "\n":
        sum += int(n)
    else:
        sums.append(sum)
        sum = 0
print(max(sums))
print(np.sum(sorted(sums)[len(sums)-3:len(sums)]))