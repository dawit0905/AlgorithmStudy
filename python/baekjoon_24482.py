import sys


def dfs(node, cnt):
    visited[node] = cnt
    cnt += 1

    for i in sorted(edges[node], reverse=True):
        if visited[i] == -1:
            dfs(i, cnt)


sys.setrecursionlimit(10**9)
n, m, r = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)

visited = [-1] * (n+1)
dfs(r, 0)

print(*visited[1:], sep='\n')
