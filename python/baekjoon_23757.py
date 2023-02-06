import sys
import heapq


n, m = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
present_list = []
for i in tmp:
    heapq.heappush(present_list, -i)

children_list = list(map(int, sys.stdin.readline().split()))

for i in children_list:
    a = -heapq.heappop(present_list)
    if a < i:
        print(0)
        exit(0)
    heapq.heappush(present_list, -(a-i))

print(1)
