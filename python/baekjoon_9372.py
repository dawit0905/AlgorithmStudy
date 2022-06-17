import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for j in range(m):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)

    que = deque()
    que.append(1)
    visited[1] = 1
    cnt = 0
    while que:
        a = que.popleft()

        for j in edges[a]:
            if visited[j] == 0:
                que.append(j)
                visited[j] = 1
                cnt += 1
    print(cnt)