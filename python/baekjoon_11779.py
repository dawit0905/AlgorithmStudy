import sys
import heapq


def dijkstra(start):
    que = [[0, start, [start]]]
    distance[start] = 0

    while que:
        dist, now, path = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for next_node, next_cost in edges[now]:
            cost = dist + next_cost
            if cost < distance[next_node]:
                distance[next_node] = cost
                near[next_node] = now
                distance_path[next_node] = path + [next_node]
                heapq.heappush(que, [cost, next_node, path+[next_node]])

    return distance, distance_path


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = sys.maxsize
distance = [sys.maxsize] * (n+1)
distance_path = [[] for _ in range(n+1)]
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a].append((b, c))

start, end = map(int, sys.stdin.readline().split())
near = [start] * (n+1)
dijkstra(start)
                               
print(distance[end])
print(len(distance_path[end]))
print(*distance_path[end])

