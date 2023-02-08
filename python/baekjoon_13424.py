import sys
import heapq


def dijkstra(start) -> list:
    que = []
    distance[start] = 0
    heapq.heappush(que, (0, start))

    while que:
        dist, now = heapq.heappop(que)

        if distance[now] < dist:
            continue

        for next_cost, next_node in edges[now]:
            cost = dist + next_cost
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(que, (cost, next_node))

    return distance


tc = int(sys.stdin.readline())
INF = sys.maxsize

for t in range(tc):
    n, m = map(int, sys.stdin.readline().split())

    edges = [[] for _ in range(n + 1)]
    total_distance = [0] * (n+1)
    total_distance[0] = INF

    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        edges[a].append((c, b))
        edges[b].append((c, a))

    k = int(sys.stdin.readline())
    k_list = list(map(int, sys.stdin.readline().split()))

    for i in k_list:
        distance = [INF] * (n + 1)
        tmp = dijkstra(i)

        for j in range(1, n+1):
            total_distance[j] += tmp[j]

    # print(total_distance)
    print(total_distance.index(min(total_distance)))



'''
    total_distance = [0] * (n+1)
    print(total_distance.index(min(total_distance[1:])))

    total_distance 을 그냥 0으로 초기화하고
    list(array) slicing을 index을 이용하는데에 하게되면
    index가 1이 아니라 0부터 시작하기 때문에 틀릴 수 밖에 없다.
    그래서 total_distacne[0]을 INF로 설정하는 방식으로 해결했다.
'''
