import sys
import heapq

n = int(sys.stdin.readline())
que = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    que.append([a, b])

que.sort()

room = []
heapq.heappush(room, que[0][1])

for i in range(1, n):
    if que[i][0] < room[0]:
        heapq.heappush(room, que[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, que[i][1])

print(len(room))