import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
INF = int(1e9)
start_node = int(sys.stdin.readline())
graph = [[] for i in range(v+1)] # [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]
distance = [INF] * (v+1)

for i in range(e):
    u,temp_v,w = map(int, sys.stdin.readline().split())
    graph[u].append((temp_v,w))

def dijkstra(start):
    que = []
    heapq.heappush(que, (0,start))
    distance[start] = 0

    while que:
        dist, now = heapq.heappop(que)

        # 기존 distance의 값이 10억이니까 작으면 이미 방문한거고, 값이 들어와도 그전에 들어온 값과 비교해서 처리
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que,(cost,i[0]))

dijkstra(start_node)

for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])