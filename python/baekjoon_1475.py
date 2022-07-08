import math
import sys


n = sys.stdin.readline().rstrip()
dictionary = {}

for i in range(len(n)):
    if int(n[i]) == 9 and 6 not in dictionary:
        dictionary[6] = 1
    elif int(n[i]) == 9:
        dictionary[6] += 1
    elif int(n[i]) not in dictionary:
        dictionary[int(n[i])] = 1
    else:
        dictionary[int(n[i])] += 1

cnt = 0
for key, value in dictionary.items():
    if key == 6:
        cnt = max(cnt, math.ceil(value/2))
    else:
        cnt = max(cnt, value)

print(cnt)