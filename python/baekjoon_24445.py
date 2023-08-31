import sys
from collections import deque


def bfs(v, e, r):
    cnt = 2
    visited = [0] * (v+1)
    visited[r] = 1
    que = deque()
    que.append(r)

    while que:
        u = que.popleft()
        for node in sorted(e[u], reverse=True):
            if not visited[node]:
                visited[node] = cnt
                cnt += 1
                que.append(node)

    print(*visited[1:],sep='\n')


n, m, r = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

bfs(n, edges, r)