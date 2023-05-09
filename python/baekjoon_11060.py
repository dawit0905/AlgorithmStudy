import sys
from collections import deque


def bfs():
    visited = [0] * (1000000)
    que = deque()
    que.append((0, 0))
    while que:
        now, cost = que.popleft()
        if now >= n-1:
            return cost
        for i in range(1, arr[now]+1):
            next = now+i
            if not visited[next]:
                que.append((next, cost+1))
                visited[next] = 1
    return -1


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer = bfs()
print(answer)

