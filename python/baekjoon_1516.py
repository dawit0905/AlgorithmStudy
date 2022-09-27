import sys
from collections import deque


def topology():
    que = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)
            dp[i] = D[i]

    while que:
        now = que.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now] + D[i], dp[i])

            if indegree[i] == 0:
                que.append(i)


n = int(sys.stdin.readline())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
dp = [0] * (n+1)
D = [0] * (n+1)
for i in range(1, n+1):
    temp = list(map(int, sys.stdin.readline().split()))
    D[i] = temp[0]
    for j in temp[1:]:
        if j == -1:
            break
        graph[j].append(i)
        indegree[i] += 1

topology()

for i in range(1, n+1):
    print(dp[i])