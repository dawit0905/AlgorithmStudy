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


n, m = map(int, sys.stdin.readline().split())
s = [[] for _ in range(n+1)]
d = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    s[a].append(b)

cnt = 0
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    if dfs(i):
        cnt += 1
print(cnt)
