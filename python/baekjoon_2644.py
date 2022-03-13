import sys
from collections import deque

def bfs(start, end):
    que = deque()
    que.append((start, 0))

    while que:
        now, cost = que.popleft()

        for node in arr[now]:
            if node == end:
                return cost+1

            if visited[node] == 0:
                que.append((node, cost+1))
                visited[node] = 1
    return -1


n = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)


print(bfs(start, end))

