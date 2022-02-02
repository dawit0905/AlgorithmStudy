'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

3
'''

import sys

n, m = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    x, k = map(int, sys.stdin.readline().split())
    graph[x][k] = 1
    graph[k][x] = 1

answer_x, answer_k = map(int,sys.stdin.readline().split())

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

distance = graph[1][answer_k] + graph[answer_k][answer_x]

if distance >= INF:
    print("-1")
else :
    print(distance)