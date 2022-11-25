import sys
from collections import deque


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    ap = find(parent, a)
    bp = find(parent, b)

    parent[max(ap, bp)] = min(ap, bp)


INF = sys.maxsize
n, m = map(int, sys.stdin.readline().split())
s, e = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]
nodes = [[] for _ in range(n+1)]
edges = []
for i in range(m):
    u, v, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, u, v))

# edges.sort(reverse=True)
edges.sort(key=lambda x: -x[0])
for cost, u, v in edges:
    if find(parent, u) == find(parent, v):
        continue

    union(parent, u, v)
    nodes[v].append((u, cost))
    nodes[u].append((v, cost))

que = deque()
visited = [0] * (n+1)
visited[s] = 1
que.append((s, INF))
answer = 0
while que:
    now, cost = que.popleft()
    if now == e:
        answer = cost
        break

    for x, distance in nodes[now]:
        if not visited[x]:
            cost = min(cost, distance)
            que.append((x, cost))
            visited[x] = 1

print(answer)
