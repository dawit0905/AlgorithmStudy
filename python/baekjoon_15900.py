import sys


def dfs(node):
    global result
    visited[node] = 1

    for i in edges[node]:
        if not visited[i]:
            depth[i] = depth[node] + 1
            dfs(i)


sys.setrecursionlimit(10**5)
n = int(sys.stdin.readline())
edges = [[] for _ in range(n+1)]
visited = [0] * (n+1)
depth = [0] * (n+1)

for i in range(n-1):
    u, v = map(int, sys.stdin.readline().split())

    edges[u].append(v)
    edges[v].append(u)

result = 0
dfs(1)
for i in range(2, n+1):
    if len(edges[i]) == 1:
        result += depth[i]

# print(depth)
print('No') if result % 2 == 0 else print('Yes')
