import sys
from collections import defaultdict
from collections import deque


def bfs(start):
    visited = [0] * (n+1)
    que = deque()
    que.append((0, start))
    visited[start] = 1
    return_cost = 1
    while que:
        cost, node = que.popleft()

        for next_node in edges[node]:

            if return_cost < cost:
                return_cost = cost

            if not visited[next_node]:
                que.append((cost+1, next_node))
                visited[next_node] = 1

    distance[start] = return_cost


n = int(sys.stdin.readline())

edges = defaultdict(list)
distance = [0] * (n+1)

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break

    edges[a].append(b)
    edges[b].append(a)

for i in range(1, n+1):
    bfs(i)


point = min(distance[1:])
print(point, distance.count(point))
for i in range(len(distance)):
    if distance[i] == point:
        print(i, end=" ")
