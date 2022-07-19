import sys
from collections import deque


def bfs():
    que = deque()
    que.append(n)
    distance[n] = 1
    cnt = 0

    while que:
        x = que.popleft()

        if x == k:
            cnt += 1

        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= MAX and (distance[nx] == 0 or distance[nx] == distance[x]+1):
                distance[nx] = distance[x] + 1
                que.append(nx)

    print(distance[k]-1)
    print(cnt)


n, k = map(int, sys.stdin.readline().split())
MAX = 100000
distance = [0] * (MAX+1)
bfs()