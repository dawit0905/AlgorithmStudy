import sys
from collections import deque


def fbfs(fire):
    fire_que = deque(fire)
    for ffx, ffy in fire_que:
        fire_visited[ffx][ffy] = 0
    # 불이 번지는게 먼저
    while fire_que:
        fx, fy = fire_que.popleft()
        for i in range(4):
            fnx = fx + dx[i]
            fny = fy + dy[i]

            if 0 <= fnx < r and 0 <= fny < c:
                if graph[fnx][fny] in ['.', 'J'] and not fire_visited[fnx][fny]:
                    fire_que.append((fnx, fny))
                    fire_visited[fnx][fny] = fire_visited[fx][fy] + 1


def bfs(x, y):
    que = deque()
    visited[x][y] = 1
    que.append((x, y))

    while que:
        x, y = que.popleft()

        if graph[x][y] != 'F' and (x == 0 or x == r-1 or y == 0 or y == c-1):
            return visited[x][y]
        # 지훈이가 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == '.' and not visited[nx][ny] and (not fire_visited[nx][ny] or visited[x][y]+1 <= fire_visited[nx][ny]):
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return 'IMPOSSIBLE'


r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(r)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

jihun = []
fire = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            jihun = [i, j]

        if graph[i][j] == 'F':
            fire.append([i, j])


fire_visited = [[0] * c for _ in range(r)]
visited = [[0] * c for _ in range(r)]
fbfs(fire)
print(bfs(jihun[0], jihun[1]))
