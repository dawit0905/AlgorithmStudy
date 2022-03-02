import sys
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0],))

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = int(1e9)
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    x, y, c = map(int, sys.stdin.readline().split())
    graph[x].append((y, c))

start, end = map(int, sys.stdin.readline().split())

dijkstra(start)

print(distance[end])




