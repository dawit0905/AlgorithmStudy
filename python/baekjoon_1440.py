import sys
from itertools import permutations


s = list(map(int, sys.stdin.readline().strip().split(':')))

time = [59, 12, 59]
cnt = 0
permu = list(permutations(time, 3))

for i in permu:
    flag = True
    for j in range(3):
        if i[j] == 12:
            if s[j] == 0:
                flag = False
                break
            if not (0 <= s[j] <= 12):
                flag = False
                break
        elif not (0 <= s[j] <= 59):
            flag = False
            break
    if flag:
        cnt += 1

print(cnt)