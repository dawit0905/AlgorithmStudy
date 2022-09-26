import sys
from collections import deque
import heapq


def topology():
    result = []
    que = []

    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(que, i)

    while que:
        now = heapq.heappop(que)
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                heapq.heappush(que, i)

    print(*result)


n, m = map(int, sys.stdin.readline().split())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

topology()

