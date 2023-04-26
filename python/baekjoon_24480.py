import sys


def dfs(start):
    global cnt
    visited[start] = cnt

    for i in sorted(edges[start], reverse=True):
        if not visited[i]:
            cnt += 1
            dfs(i)


sys.setrecursionlimit(10**9)
n, m, r = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)

cnt = 1
visited = [0] * (n+1)
dfs(r)

print(*visited[1:], sep='\n')
