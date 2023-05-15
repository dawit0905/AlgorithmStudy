import sys
from collections import defaultdict

n = int(sys.stdin.readline())

count = 0
dic = defaultdict()

for i in range(n):
    s = sys.stdin.readline().strip()
    tmp = s[:1]
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

arr = dic.items()

answer = []
for s, cnt in arr:
    if cnt >= 5:
        answer.append(s)

answer.sort()
if answer == []:
    answer.append('PREDAJA')

print(*answer, sep='')