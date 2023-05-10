import sys


'''
언제 answer에 1을 더해주는가?
이미 방문했던 곳에 도착했을 때 마침 flag_map[x][y] == idx일 경우일 때다. 즉 최초로 cycle이 발견되는 순간이다. 
방문했던 곳에 도착하더라도 flag_map[x][y] != idx이면 이미 형성된 cycle에 진입하는 경우이므로 answer를 더해주면 안된다.
'''

def move(x, y, idx):
    global answer

    # 이미 방문한 곳이라면
    if flag_map[x][y] != -1:
        if flag_map[x][y] == idx:
            answer += 1
        return

    # 방문하지 않았다면
    flag_map[x][y] = idx
    i = direction.index(graph[x][y])
    move(x + dx[i], y + dy[i], idx)


n, m = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline().strip() for _ in range(n)]
flag_map = [[-1 for _ in range(m)] for _ in range(n)]

direction = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

idx = 0
answer = 0
for i in range(n):
    for j in range(m):
        move(i, j, idx)
        idx += 1

print(answer)