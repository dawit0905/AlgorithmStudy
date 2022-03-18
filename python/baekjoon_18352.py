import sys
import heapq


def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    temp = []
    while que:
        dist, now = heapq.heappop(que)

        if distance[now] == k:
            temp.append(now)

        if distance[now] < dist:
            continue

        for node_num, node_cost in graph[now]:
            cost = dist + node_cost
            if cost < distance[node_num]:
                distance[node_num] = cost
                heapq.heappush(que, (cost, node_num))
    return temp

n, m, k, x = map(int, sys.stdin.readline().split())
INF = int(1e9)
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))


answer = dijkstra(x)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for num in answer:
        print(num)




