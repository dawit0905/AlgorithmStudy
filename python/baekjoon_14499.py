import sys


def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 동
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    # 서
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    # 북
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    # 남
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


n, m, x, y, k = map(int, sys.stdin.readline().split())
graph = []
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
k_list = list(map(int, sys.stdin.readline().split()))

nx, ny = x, y
for i in k_list:
    nx += dx[i]
    ny += dy[i]

    if 0 <= nx < n and 0 <= ny < m:
        turn(i)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[-1]
        else:
            dice[-1] = graph[nx][ny]
            graph[nx][ny] = 0

        print(dice[0])
    else:
        nx -= dx[i]
        ny -= dy[i]
