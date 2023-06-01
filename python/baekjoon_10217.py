import sys
import heapq


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, 0, start))

    while heap:
        cur_dist, cur_cost, cur_node = heapq.heappop(heap)

        if dp[cur_cost][cur_node] < cur_dist:
            continue

        for to_node, to_cost, to_dist in graph[cur_node]:
            d = cur_dist + to_dist
            c = cur_cost + to_cost

            if c <= cost and d < dp[c][to_node]:
                for i in range(c, cost+1):
                    if dp[i][to_node] > d:
                        dp[i][to_node] = d
                    else:
                        break
                heapq.heappush(heap, (d, c, to_node))


t = int(sys.stdin.readline())
INF = float('inf')

for _ in range(t):
    n, cost, k = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    dp = [[INF] * (n) for _ in range(cost + 1)]
    for i in range(k):
        u, v, c, d = map(int, sys.stdin.readline().split())
        u -= 1; v -= 1
        graph[u].append((v,c,d))

    dijkstra(0)
    print(dp[cost][n-1] if dp[cost][n-1] != INF else "Poor KCM")



