import sys


# 공기 청정기 위치 찾기
def find_air_cleaner():
    for i in range(r):
        if graph[i][0] == -1:
            return i


r, c, t = map(int, sys.stdin.readline().split())
graph = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]


for i in range(r):
    graph.append(list(map(int, sys.stdin.readline().split())))

air_cleaner_i = find_air_cleaner()

for _ in range(t):
    dust = []
    for i in range(r):
        for j in range(c):
            # 미세먼지 발견, 미세먼지 확산
            if graph[i][j] > 0:
                dust.append((i, j, graph[i][j]))

    for i, j, dust_value in dust:
        volume = dust_value//5

        if volume == 0:
            continue

        spread_cnt = 0
        for k in range(4):
            nx = dx[k] + i
            ny = dy[k] + j
            if 0 <= nx < r and 0 <= ny < c:
                if nx ==air_cleaner_i and ny == 0:
                    continue
                if nx == (air_cleaner_i+1) and ny == 0:
                    continue
                spread_cnt += 1
                graph[nx][ny] += volume

        graph[i][j] -= volume * spread_cnt

    # print('미세먼지 확산 후')
    # for aa in graph:
    #     print(*aa)

        # 아래쪽으로
    for i in range(air_cleaner_i - 1, 0, -1):
        graph[i][0] = graph[i - 1][0]

    #  <-
    for j in range(c - 1):
        graph[0][j] = graph[0][j + 1]

    # 위로
    for i in range(air_cleaner_i):
        graph[i][c - 1] = graph[i + 1][c - 1]

    # ->
    for j in range(c - 1, 0, -1):
        graph[air_cleaner_i][j] = graph[air_cleaner_i][j - 1]
    # 공기청정기에서 나온 바람
    graph[air_cleaner_i][1] = 0

    # 아래

    # 위로
    for i in range(air_cleaner_i + 2, r - 1):
        graph[i][0] = graph[i + 1][0]

    #  <-
    for j in range(c - 1):
        graph[r - 1][j] = graph[r - 1][j + 1]

    # 아래쪽으로
    for i in range(r - 1, air_cleaner_i + 1, -1):
        graph[i][c - 1] = graph[i - 1][c - 1]

    # ->
    for j in range(c - 1, 0, -1):
        graph[air_cleaner_i + 1][j] = graph[air_cleaner_i + 1][j - 1]
    # 공기청정기에서 나온 바람
    graph[air_cleaner_i + 1][1] = 0

    # print('공기청정기 공기 이동 후')
    # for aa in graph:
    #     print(*aa)


total_dust = 0
for i in range(r):
    total_dust += sum(graph[i])

print(total_dust+2)