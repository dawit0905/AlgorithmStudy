import sys
import heapq


n, k = map(int, sys.stdin.readline().split())
jewelry = []
bags = []
for i in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(jewelry, [m, v])

for i in range(k):
    c = int(sys.stdin.readline())
    bags.append(c)

bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jewelry)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jewelry:
        break

print(answer)

