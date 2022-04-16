import sys
from collections import deque


def bfs(Dx, Dy):
    while que:
        x, y = que.popleft()
        if graph[Dx][Dy] == 'S':
            return distance[Dx][Dy]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c:
                if(graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] + 1
                    que.append((nx, ny))
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    que.append((nx, ny))
    return "KAKTUS"


r, c = map(int, sys.stdin.readline().split())
graph = []
distance = [[0] * c for _ in range(r)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
que = deque()

for i in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            que.append((i,j))
        elif graph[i][j] == 'D':
            Dx, Dy = i, j

for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            que.append((i,j))

print(bfs(Dx,Dy))
