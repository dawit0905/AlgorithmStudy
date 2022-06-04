import sys


def dfs(start):
    if visited[start] == 1:
        return 0
    visited[start] = 1
    for i in s[start]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = start
            return 1
    return 0


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sa = [0]
sb = [0]
result = []
for i in range(n):
    if arr[0] % 2 == arr[i] % 2:
        sa.append(arr[i])
    else:
        sb.append(arr[i])

e = [True for i in range(2000)]
e[1] = False
for i in range(2, 2000//2):
    if e[i] == True:
        for j in range(i*2, 2000, i):
            e[j] = False

s = [[] for i in range(len(sa))]
for i in range(1, len(sa)):
    for j in range(1, len(sb)):
        if e[sa[i] + sb[j]]:
            s[i].append(j)

for i in s[1]:
    d = [0 for _ in range(len(sb))]
    d[i] = 1
    cnt = 1
    for j in range(1, len(sa)):
        visited = [0 for _ in range(len(sa))]
        visited[1] = 1
        cnt += dfs(j)
    if cnt == n//2:
        result.append(sb[i])

if result:
    result.sort()
    print(*result)
else:
    print(-1)










