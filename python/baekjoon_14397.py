import sys


def check(x, y):
    global result
    for i in range(6):
        nx = x + dx[i]
        if x % 2 == 0:
            ny = y + dy_even[i]
        else:
            ny = y + dy_odd[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == '.':
                result += 1


n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().strip()))

land = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == '#':
            land.append((i, j))

dx = [-1,-1,0,0,1,1]
dy_odd = [0,1,-1,1,0,1]
dy_even = [-1,0,-1,1,-1,0]
result = 0
for x, y in land:
    check(x, y)

print(result)
