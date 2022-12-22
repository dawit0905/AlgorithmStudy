import sys
from collections import Counter


T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

answer = 0
c = Counter()  
for i in range(n):
    for j in range(i, n):
        c[sum(A[i:j + 1])] += 1

for i in range(m):
    for j in range(i, m):
        t = T - sum(B[i:j + 1])
        answer += c[t]
print(answer)
