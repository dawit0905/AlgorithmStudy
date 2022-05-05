import sys
from collections import deque

def bfs(f,s,g,u,d):

    que = deque()
    que.append(s)
    floor[s] = 1

    while que:
        now = que.popleft()
        if now == g:
            return floor[g] - 1

        up = now+u
        down = now-d

        # 위로가기
        if 1 <= up <= f and floor[up] == 0:
            que.append(up)
            floor[up] = floor[now] + 1
        # 아래로 가기
        if 1 <= down <= f and floor[down] == 0:
            que.append(down)
            floor[down] = floor[now] + 1

    return 'use the stairs'


f, s, g, u, d = map(int, sys.stdin.readline().split())
floor = [0] * (f+1)
print(bfs(f,s,g,u,d))