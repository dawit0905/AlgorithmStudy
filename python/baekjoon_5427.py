import sys
from collections import deque


def fire():
    fire_len = len(fire_que)
    for j in range(fire_len):
        x, y = fire_que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] == '.':
                    fire_que.append((nx, ny))
                    arr[nx][ny] = '*'


def bfs():
    while que:
        q_len = len(que)
        for j in range(q_len):
            x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and distance[nx][ny] == 0:
                    if arr[nx][ny] == '.':
                        que.append((nx, ny))
                        distance[nx][ny] = distance[x][y]+1
                elif nx < 0 or nx >= h or ny < 0 or ny >= w:
                    print(distance[x][y] + 1)
                    return
        fire()
    print("IMPOSSIBLE")
    return



t = int(sys.stdin.readline())
for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    arr = []
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    distance = [[0] * w for _ in range(h)]
    que = deque()
    fire_que = deque()
    for _ in range(h):
        arr.append(list(sys.stdin.readline().rstrip()))

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                que.append((i, j))
                arr[i][j] = '.'
            elif arr[i][j] == '*':
                fire_que.append((i, j))

    fire()
    bfs()