import sys
from collections import deque


dx = [0,0,-1,1,0,0]
dy = [-1,1,0,0,0,0]
dz = [0,0,0,0,-1,1]

while True:
    l, r, c = map(int, sys.stdin.readline().split())
    if l == 0 and r == 0 and c == 0:
        break

    graph = [[] * r for _ in range(l)]

    for i in range(l):
        for j in range(r):
            graph[i].append(list(map(str, sys.stdin.readline().rstrip())))
        sys.stdin.readline()

    start_xy = ()
    end_xy = ()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    start_xy = (i,j,k)
                if graph[i][j][k] == 'E':
                    end_xy = (i,j,k)

    # bfs
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    que = deque()
    z,y,x = start_xy
    visited[z][y][x] = 1
    que.append((z,y,x))

    while que:
        z, y, x = que.popleft()

        for i in range(6):
            nz = dz[i] + z
            ny = dy[i] + y
            nx = dx[i] + x

            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c and not visited[nz][ny][nx] and graph[nz][ny][nx] != '#':
                que.append((nz,ny,nx))
                visited[nz][ny][nx] = visited[z][y][x] + 1

    z, y, x = end_xy
    if visited[z][y][x] == 0:
        print("Trapped!")
    else:
        print(f"Escaped in {visited[z][y][x]-1} minute(s).")

