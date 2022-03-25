from collections import deque
import sys


def topology_sort():
    q = deque()

    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)
            dp[i] = D[i]

    while q:
        now = q.popleft()

        for i in graph[now]:
            inDegree[i] -= 1
            dp[i] = max(dp[now] + D[i], dp[i])

            if inDegree[i] == 0:
                q.append(i)

    return dp[W]


T = int(sys.stdin.readline())
for _ in range(T):
    n, k = map(int, sys.stdin.readline().split())
    D = [0] + list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(n + 1)]
    inDegree = [0] * (n + 1)
    dp = [0] * (n+1)

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        inDegree[b] += 1
    W = int(sys.stdin.readline())
    print(topology_sort())
