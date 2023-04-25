import sys


def dfs(start):
    global cnt
    visited[start] = cnt
    cnt += 1
    for node in sorted(edges[start]):
        if not visited[node]:
            dfs(node)


sys.setrecursionlimit(int(10**9))
n, m, r = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)

visited = [0] * (n+1)
cnt = 1
dfs(r)

print(*visited[1:], sep='\n')
