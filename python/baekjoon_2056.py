import sys
from collections import deque


def topology():
    que = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)

    while que:
        now = que.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now] + D[i], dp[i])

            if indegree[i] == 0:
                que.append(i)

    return max(dp)


n = int(sys.stdin.readline())
indegree = [0] * (n+1)
dp = [0] * (n+1)
D = [0] * (n+1)
graph = [[] for i in range(n+1)]
for i in range(1, n+1):
    arr = list(map(int, sys.stdin.readline().split()))
    tmp = arr[1]
    D[i] = arr[0]
    dp[i] = arr[0]
    # indegree[i] += arr[1]
    for j in range(1, tmp+1):
        graph[arr[j+1]].append(i)
        indegree[i] += 1

print(topology())