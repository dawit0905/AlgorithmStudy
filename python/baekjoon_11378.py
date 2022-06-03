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


n, m, k = map(int, sys.stdin.readline().split())
s = [[] for _ in range(n+1)]
d = [0 for _ in range(m+1)]
cnt = 0

for i in range(1, n+1):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in arr[1:]:
        s[i].append(j)

for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    if dfs(i):
        cnt += 1

for i in range(1, n+1):
    while k > 0:
        visited = [0 for _ in range(n+1)]
        if dfs(i):
            cnt += 1
            k -= 1
        else:
            break

print(cnt)
