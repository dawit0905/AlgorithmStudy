import sys
from collections import deque


def bfs(start):
    que = deque()
    num = 2
    visited[start] = 1
    que.append(start)

    while que:
        node = que.popleft()

        for next_node in sorted(edges[node]):
            if visited[next_node]:
                continue

            visited[next_node] = num
            num += 1
            que.append(next_node)


n, m, r = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)


visited = [0] * (n+1)

bfs(r)
print(*visited[1:], sep='\n')
