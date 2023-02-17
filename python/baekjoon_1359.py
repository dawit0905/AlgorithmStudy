import sys
from itertools import combinations


n, m, k = map(int, sys.stdin.readline().split())
combis = list(combinations(range(n), m))
ans = 0

for combi in combis:
    cnt = 0
    for i in range(m):
        if combi[i] < m:
            cnt += 1
    if cnt >= k:
        ans += 1

print(ans / len(combis))
