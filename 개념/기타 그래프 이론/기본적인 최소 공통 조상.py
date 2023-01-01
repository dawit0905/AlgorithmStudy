import sys


def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:
            continue
        parent[y] = x
        dfs(y, depth+1)


def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


sys.setrecursionlimit(int(1e5))
n = int(sys.stdin.readline())

parent = [0] * (n+1)
d = [0] * (n+1)
c = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)

m = int(sys.stdin.readline())

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a, b))




