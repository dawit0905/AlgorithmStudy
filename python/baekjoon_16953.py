import sys
from collections import deque

def bfs(start, end):
    que = deque()
    que.append((start, 1))

    while que:
        now, cost = que.popleft()

        if now == end:
            return cost

        if now <= b:
            que.append((now*2, cost+1))
            que.append((now*10+1, cost+1))

    return -1


a, b = map(int, sys.stdin.readline().split())

print(bfs(a, b))