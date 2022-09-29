import sys
from collections import deque


def topology():
    que = deque()
    result = []

    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)
            result.append(i)

    while que:
        now = que.popleft()

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                que.append(i)
                result.append(i)

    if len(result) != n:
        print(0)
    else:
        for i in result:
            print(i)


n, m = map(int, sys.stdin.readline().split())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    arr = list(map(int, sys.stdin.readline().split()))

    for j in range(1, arr[0]+1):
        for t in range(j-1, 0, -1):
            graph[arr[t]].append(arr[j])
            indegree[arr[j]] += 1

topology()
