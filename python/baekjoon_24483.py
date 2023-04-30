import sys


def dfs(node, cnt):
    global ordered
    visited[node] = cnt
    order[node] = ordered
    ordered += 1

    for i in sorted(edges[node]):
        if visited[i] == -1:
            dfs(i, cnt+1)


sys.setrecursionlimit(10**9)
n, m, r = map(int, sys.stdin.readline().split())

edges = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)

visited = [-1] * (n+1)
ordered = 1
order = [0] * (n+1)
dfs(r, 0)

# print(visited)
# print(order)
result = 0
for i in range(1, n+1):
    if visited[i] != -1:
        result += visited[i] * order[i]

print(result)